import argparse
from openai import OpenAI
import pandas as pd
import datetime
import os

def get_api_key():
    try:
        with open('api_key.txt', 'r', encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: API key file 'api_key.txt' not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading API key: {e}")
        exit(1)

client = OpenAI(
    api_key=get_api_key(),
)

def read_rubric_and_key(rubric_file, answer_key_file):
    # Read the rubric
    rubric_df = pd.read_excel(rubric_file)
    rubric = rubric_df.iloc[0].to_dict()  # Assuming the first row contains rubric content
    
    # Read the answer key
    answer_key_df = pd.read_excel(answer_key_file)
    answer_key = answer_key_df.iloc[0].to_dict()  # Assuming the first row contains answer key content
    
    return rubric, answer_key

def log_interaction(log_file, messages, response):
    # Logs the entire interaction with ChatGPT to a file.
    with open(log_file, 'a', encoding="utf-8") as log:
        log.write("----- Interaction -----\n")
        for message in messages:
            log.write(f"{message['role']}: {message['content']}\n")
        log.write(f"Response: {response}\n")
        log.write("-----------------------\n\n")

def grade_section_with_key(rubric_content, answer_key_content, section_content, section_name, temperature, top_p, log_file):
    # Grades a section using both the rubric and answer key for that section, and logs the conversation.
    rubric_text = rubric_content.get(section_name.lower(), "No rubric available for this section.")
    answer_key_text = answer_key_content.get(section_name.lower(), "")
    
    # Prepare the initial prompt to grade the section
    messages = [
        {"role": "system", "content":   f"I am a medical educator and I would like your help grading an assignment. "
                                        f"My students recently completed an activity where they interviewed a patient about their symptoms. "
                                        f"I have made a scoring rubric that includes the information that should be reported in their post-interview note. "
                                        f"The rubric is broken into individual steps. To help you out, I just want you to score each individual section that I will provide you one by one."
                                        f"Please score each individual section that I provide you based off the rubric and the answer key. Please think through this step-by-step."
                                        f"Please place their final score after your explanation all by itself as an integer with no markup"},
        {"role": "user", "content": f"Refer to the rubric: {rubric_text}. "
                                    f"Here is the answer key for {section_name}: {answer_key_text}. "
                                    f"Please evaluate the following {section_name} and provide a score: "
                                    f"{section_content}"}
    ]

    # Send the initial request to ChatGPT
    response = client.chat.completions.create(  
        model="gpt-4o-mini",  
        messages=messages,
        temperature=temperature,
        top_p=top_p
    )

    # Get the response content (the full explanation)
    score_text = response.choices[0].message.content.strip()

    # Log the conversation for tracking
    log_interaction(log_file, messages, score_text)

    # Now, prepare the second prompt to ask for only the numeric score, including the explanation from the first call
    extraction_prompt = [
        {"role": "system", "content": "Your role is to help me complete this very simple task."},
        {"role": "user", "content": f"For the following message: '{score_text}', please extract and output only the numeric score as an integer without any explanation or markdown."}
    ]

    # Send the second request to ChatGPT to extract just the numeric score
    response = client.chat.completions.create(  
        model="gpt-4o",  
        messages=extraction_prompt,
        temperature=temperature,
        top_p=top_p
    )

    # Get the numeric score from the response
    numeric_score = response.choices[0].message.content.strip()

    # Attempt to convert the score to an integer
    try:
        numeric_score = int(numeric_score)  # Try converting to integer
    except ValueError:
        print(f"Warning: Could not convert the response to an integer. Saving explanation only.")
        numeric_score = None  # If conversion fails, return None for the numeric score

    return score_text, numeric_score  # Return both the explanation and the numeric score

def process_excel_file_with_key(excel_file, rubric_content, answer_key_content, output_file, temperature=0.5, top_p=1.0):
    # Processes each row in the Excel file, grades the relevant sections, and appends the scores.
    df = pd.read_excel(excel_file)
    
    # Create a log file with the same name as the output file but with a .log extension
    log_file = os.path.splitext(output_file)[0] + ".log"
    
    # Columns expected in the Excel file
    sections = ['hpi', 'pex', 'sum', 'ddx', 'support', 'plan']
    section_headers = {
        'hpi': 'History of Present Illness',
        'pex': 'Physical Examination',
        'sum': 'Summary',
        'ddx': 'Differential Diagnosis',
        'support': 'Supporting Information',
        'plan': 'Plan'
    }

    for index, row in df.iterrows():
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Print the progress message with a timestamp
        print(f"{current_time} - Processing row {index + 1}/{len(df)}...")

        # Iterate through each section (HPI, PEX, etc.) and grade it
        for section in sections:
            section_content = row[section]
            if pd.notna(section_content):  # Only process if the section is not empty
                explanation, numeric_score = grade_section_with_key(rubric_content, answer_key_content, section_content, section, temperature, top_p, log_file)
                df.at[index, f'{section}_gpt_explanation'] = explanation
                df.at[index, f'{section}_gpt_score'] = numeric_score
        
        # For the "organization" section, combine all sections with headers and new lines
        combined_sections = ""
        for section in sections:
            if pd.notna(row[section]):  # Only add sections that have content
                combined_sections += f"{section_headers[section]}:\n{row[section]}\n\n"
        
        # Grade the combined "organization" section
        org_explanation, org_score = grade_section_with_key(rubric_content, {}, combined_sections, "org", temperature, top_p, log_file)  # Org doesn't need answer key
        df.at[index, 'org_gpt_explanation'] = org_explanation
        df.at[index, 'org_gpt_score'] = org_score
    
    # Save the new Excel file with the scores appended
    df.to_excel(output_file, index=False)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - Grading completed. Results saved to {output_file}. Log saved to {log_file}.")

if __name__ == '__main__':
    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description='Grade OSCE notes from an Excel file using OpenAI with a rubric and answer key.')
    parser.add_argument('rubric_excel', type=str, help='The path to the rubric Excel file')
    parser.add_argument('answer_key_excel', type=str, help='The path to the answer key Excel file')
    parser.add_argument('notes_file', type=str, help='The path to the Excel file containing student notes')
    parser.add_argument('output_file', type=str, help='The path to save the output Excel file with grades')
    parser.add_argument('--temperature', type=float, default=0.5, help='The temperature setting for the OpenAI API (default: 0.5)')
    parser.add_argument('--top_p', type=float, default=1.0, help='The top_p setting for the OpenAI API (default: 1.0)')
    
    args = parser.parse_args()

    # Read the rubric and answer key files
    rubric_content, answer_key_content = read_rubric_and_key(args.rubric_excel, args.answer_key_excel)

    # Process the Excel file and append scores
    process_excel_file_with_key(args.notes_file, rubric_content, answer_key_content, args.output_file, args.temperature, args.top_p)
