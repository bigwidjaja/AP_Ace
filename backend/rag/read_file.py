import fitz  
import os

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


if __name__ == '__main__':
    pdf_text = extract_pdf_text("pdfs/apUSGovfrq.pdf")
    markdown_text = text_to_markdown(pdf_text)

    with open('sample.md', 'w') as f:
        f.write(markdown_text)

directory_path = os.path.expanduser("~/ap_ace/backend/rag/markdown_directory")  # Store in home directory
os.makedirs(directory_path, exist_ok=True)
os.replace("sample.md", os.path.join(directory_path, "sample.md"))


    
print(markdown_text)

