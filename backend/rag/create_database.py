from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import ollama
import os
import shutil
import fitz  
from pdfminer.high_level import extract_text

chroma_path = "chroma"
data_path = "books/pdf"

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

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents():
    loader = DirectoryLoader(data_path, glob='*.md')
    documents = loader.load()
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 500,
        length_function = len,
        add_start_index = True,
        )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks
    
def save_to_chroma(chunks: list[Document]):
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)

    embeddings = OllamaEmbeddings(model="deepseek-r1:7b")  # Change "mistral" to your preferred model
    db = Chroma.from_documents(
        chunks, embeddings, persist_directory=chroma_path
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {chroma_path}.")

if __name__ == '__main__':
    pdf_text = extract_pdf_text("apUSGovfrq.pdf")
    markdown_text = text_to_markdown(pdf_text)
    print(markdown_text)




