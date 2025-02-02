import argparse
import pandas as pd
import datetime
import os
import config
from openai import OpenAI

def get_api_key():
    try:
        with open(config.API_KEY_FILE, 'r', encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: API key file not found.")
        exit(1)

client = OpenAI(api_key=get_api_key())

def read_rubric_and_key(rubric_file, answer_key_file):
    rubric_df = pd.read_excel(rubric_file)
    rubric = rubric_df.iloc[0].to_dict()
    answer_key_df = pd.read_excel(answer_key_file)
    answer_key = answer_key_df.iloc[0].to_dict()
    return rubric, answer_key

def log_interaction(log_file, messages, response):
    with open(log_file, 'a', encoding="utf-8") as log:
        log.write("----- Interaction -----\n")
        for message in messages:
            log.write(f"{message['role']}: {message['content']}\n")
        log.write(f"Response: {response}\n")
        log.write("-----------------------\n\n")

def grade_section_with_key(rubric_content, answer_key_content, section_content, section_name, log_file):
    rubric_text = rubric_content.get(section_name.lower(), "No rubric available for this section.")
    answer_key_text = answer_key_content.get(section_name.lower(), "")
    messages = [
        {"role": "system", "content": config.GRADING_PROMPT},
        {"role": "user", "content": f"Refer to the rubric: {rubric_text}.\nHere is the answer key for {section_name}: {answer_key_text}.\nPlease evaluate the following {section_name} and provide a score: {section_content}"}
    ]
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=messages,
        temperature=config.TEMPERATURE,
        top_p=config.TOP_P
    )
    score_text = response.choices[0].message.content.strip()
    log_interaction(log_file, messages, score_text)
    extraction_prompt = [
        {"role": "system", "content": "Your role is to help me complete this very simple task."},
        {"role": "user", "content": f"For the following message: '{score_text}', please extract and output only the numeric score as an integer without any explanation or markdown."}
    ]
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=extraction_prompt,
        temperature=config.TEMPERATURE,
        top_p=config.TOP_P
    )
    numeric_score = response.choices[0].message.content.strip()
    try:
        numeric_score = int(numeric_score)
    except ValueError:
        print("Warning: Could not convert the response to an integer. Saving explanation only.")
        numeric_score = None
    return score_text, numeric_score

def process_excel_file_with_key(excel_file, rubric_content, answer_key_content, output_file):
    df = pd.read_excel(excel_file)
    log_file = os.path.splitext(output_file)[0] + ".log"
    sections = ['hpi', 'pex', 'sum', 'ddx', 'support', 'plan']
    for index, row in df.iterrows():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} - Processing row {index + 1}/{len(df)}...")
        for section in sections:
            section_content = row[section]
            if pd.notna(section_content):
                explanation, numeric_score = grade_section_with_key(rubric_content, answer_key_content, section_content, section, log_file)
                df.at[index, f'{section}_gpt_explanation'] = explanation
                df.at[index, f'{section}_gpt_score'] = numeric_score
    df.to_excel(output_file, index=False)
    print(f"Grading completed. Results saved to {output_file}. Log saved to {log_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Grade OSCE notes from an Excel file using OpenAI with a rubric and answer key.')
    parser.add_argument('--rubric', type=str, default=config.DEFAULT_RUBRIC_PATH, help='The path to the rubric Excel file')
    parser.add_argument('--answer_key', type=str, default=config.DEFAULT_NOTES_PATH, help='The path to the answer key Excel file')
    parser.add_argument('--notes', type=str, default=config.DEFAULT_NOTES_PATH, help='The path to student notes')
    parser.add_argument('--output', type=str, default=config.DEFAULT_OUTPUT_PATH, help='The path to save the output Excel file with grades')
    args = parser.parse_args()
    rubric_content, answer_key_content = read_rubric_and_key(args.rubric, args.answer_key)
    process_excel_file_with_key(args.notes, rubric_content, answer_key_content, args.output)
