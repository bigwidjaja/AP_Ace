from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import os
import shutil

chroma_path = "chroma"
data_path = "data/pdfs"

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
        chunk_size = 500,
        chunk_overlap = 250,
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

    embeddings = OllamaEmbeddings(model="deepseek-r1:7b")
    db = Chroma.from_documents(
        chunks, embeddings, persist_directory=chroma_path
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {chroma_path}.")

def main():
    generate_data_store()

