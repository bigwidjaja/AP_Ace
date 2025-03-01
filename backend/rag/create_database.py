from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
import ollama
import os
import shutil

chroma_path = "chroma"
data_path = "books/pdf"

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
    print(documents.page_content)
    print(documents.metadata)

    return chunks

def save_to_chrome(chunks: list[Document]):
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)

    db = Chroma.from_documents(
            chunks, 



