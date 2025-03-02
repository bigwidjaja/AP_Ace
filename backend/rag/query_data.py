import argparse
import ollama
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based on the following context

{context}

---

Answer the question based on the above context {question}
"""
class OllamaEmbeddings:
    def embed_query(self, text):
        response = ollama.embeddings(model="deepseek-r1:7b", prompt=text)
        return response["embedding"]
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type = str, help = "The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    embedding_function = OllamaEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function = embedding_function)

    results = db.similarity_search_with_relevance_scores(query_text, k=5)
    if len(results) == 0 or results[0][1] < 0.7:
        print("Unable to find results")
        return
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

if __name__ == "__main__":
    main()


