from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import ollama
import os
import shutil

chroma_path = "chroma"
data_path = "books/pdf"

def generate_data_store():
    documents = load_documents()
    
# Splitting text here
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 500,
    add_start_index = True,
        )

chunks = text_splitter.split_documents(documents)

