from langchain_text_splitters import RecursiveCharacterTextSplitter

# Splitting text here
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 500,
    add_start_index = True,
        )

chunks = text_splitter.split_documents(documents)
