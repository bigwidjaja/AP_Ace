import fitz  
import os
from pathlib import Path
from testapp import getClass

def extract_pdf_text(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text("text")
    return text

def text_to_markdown(text):
    lines = text.splitlines()
    markdown = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(" " * 4): 
            markdown += f"- {line.strip()}\n"
        elif line.isupper() and len(line) < 50:
            markdown += f"# {line}\n"
        else:
            markdown += line + "\n"
    return markdown

def find_file(filename, search_path):
    search_path = Path(search_path)
    for file in search_path.rglob(filename):  # Recursively search for the file
        return file
    return None  # Return None if file is not found

if __name__ == '__main__':
    pdf_directory = "pdfs"
    class_name = getClass.class_name 
    file_string = class_name.lower().split() 
    
    file_path = find_file(file_string, pdf_directory)
    
    if file_path:
        print(f"File found: {file_path}")
        try:
            pdf_text = extract_pdf_text(file_path)
            markdown_text = text_to_markdown(pdf_text)
        except Exception as error:
            print(f"Error processing PDF: {error}")
            exit()

        # Write to markdown file
        with open('sample.md', 'w') as f:
            f.write(markdown_text)

        # Move markdown file to desired directory
        directory_path = os.path.expanduser("~/ap_ace/backend/rag/markdown_directory")
        os.makedirs(directory_path, exist_ok=True)
        os.replace("sample.md", os.path.join(directory_path, "sample.md"))

        print(markdown_text)
    else:
        print("File not found.")

