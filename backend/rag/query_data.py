import argparse
import requests
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings

CHROMA_PATH = "chroma"
API_URL = "http://127.0.0.1:11434/api/generate"

PROMPT_TEMPLATE = """
Generate three practice problems based on the following context. 
Ensure they are clear, relevant, and progressively challenging. Note. DONT SOLVE THESE PROBLEMS.
ONLY CREATE NEW ONES BASED ON THESE ONES.


{context}

---

Practice problems:
"""

def answer_prompt(prompt):
    data = { 
            "model": "deepseek-r1:7b",
            "prompt": prompt,
            "stream": False }

    response = requests.post(API_URL, json=data)
    response_json = response.json()
    return response_json.get("response", "Error generating response")

def main():
    '''parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The topic to generate practice problems for.")
    args = parser.parse_args()
    query_text = args.query_text'''

    embedding_function = OllamaEmbeddings(model="deepseek-r1:7b")
    query_text = "derivative of sin(x)"
    query_embedding = embedding_function.embed_query(query_text)
    print("Query Embedding (first 10 values):", query_embedding[:10])
    print("Embedding Length:", len(query_embedding))
    
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    print(f"Database contains {db._collection.count()} documents.")    

    results = db.similarity_search_with_relevance_scores(query_text, k=5)

    print("Results with scores:")
    for doc, score in results:
        print(f"Score: {score}, Content: {doc.page_content}")

    if len(results) == 0 or results[0][1] < 0.7:
        print("Unable to find relevant content for practice problems.")
        

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text)
    print("Generated prompt:\n", prompt)

    response_text = answer_prompt(prompt)

    sources = [doc.metadata.get("source", "Unknown") for doc, _score in results]
    formatted_response = f"Generated Practice Problems:\n{response_text}\n\nSources: {sources}"
    print(formatted_response)

if __name__ == "__main__":
    main()