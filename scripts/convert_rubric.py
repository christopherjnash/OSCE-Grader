import pandas as pd
import os
from pdfminer.high_level import extract_text
from docx import Document

def convert_pdf_to_text(pdf_path):
    """Extracts text from a PDF file."""
    return extract_text(pdf_path)

def convert_docx_to_text(docx_path):
    """Extracts text from a DOCX file."""
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def save_text_to_excel(text, output_path):
    """Saves extracted text into an Excel file."""
    df = pd.DataFrame({'Rubric': text.split('\n')})
    df.to_excel(output_path, index=False)

def save_text_to_csv(text, output_path):
    """Saves extracted text into a CSV file."""
    df = pd.DataFrame({'Rubric': text.split('\n')})
    df.to_csv(output_path, index=False)

def convert_rubric(input_file, output_file):
    """Converts a rubric from PDF or DOCX to structured Excel or CSV."""
    ext = os.path.splitext(input_file)[-1].lower()
    
    if ext == ".pdf":
        text = convert_pdf_to_text(input_file)
    elif ext == ".docx":
        text = convert_docx_to_text(input_file)
    else:
        print("Unsupported file format. Please provide a PDF or DOCX.")
        return
    
    output_ext = os.path.splitext(output_file)[-1].lower()
    if output_ext == ".xlsx":
        save_text_to_excel(text, output_file)
    elif output_ext == ".csv":
        save_text_to_csv(text, output_file)
    else:
        print("Unsupported output format. Please specify .xlsx or .csv.")
        return
    
    print(f"Conversion successful! Output saved to {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert rubric from PDF or DOCX to Excel or CSV format.")
    parser.add_argument("input_file", type=str, help="Path to the input PDF or DOCX file.")
    parser.add_argument("output_file", type=str, help="Path to the output Excel (.xlsx) or CSV (.csv) file.")
    args = parser.parse_args()
    
    convert_rubric(args.input_file, args.output_file)
