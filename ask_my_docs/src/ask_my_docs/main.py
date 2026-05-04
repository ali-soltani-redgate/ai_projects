from pathlib import Path

import ollama
import chromadb


TEST_CASES = [
    {
        "question": "What is RAG?",
        "expected": "Retrieval-Augmented Generation",
    },
    {
        "question": "What is chunking strategy?",
        "expected": "splitting documents into smaller pieces",
    },
    {
        "question": "How does RAG reduce hallucination?",
        "expected": "grounded in retrieved facts",
    },
]


def main():
    collection = create_vector_store()
    evaluate(collection)


def create_vector_store():
    # 1. Load documents from the "docs" directory
    content = load_documents()

    # 2. Chunk the text into smaller pieces (e.g. 50 tokens, with overlap)
    chunks = chunk_text(content)

    # 3. Embed the chunks using a simple embedding method (e.g. TF-IDF, or a pre-trained model)
    embeddings = embed_chunks(chunks)
    print(
        f"Embedded {len(embeddings)} chunks, dimension: {len(embeddings[0])}")

    # 4. Store the embeddings in a vector database (e.g. chromadb, FAISS, Pinecone, or a simple in-memory structure)
    collection = store_in_chroma(chunks, embeddings)
    return collection

def evaluate(collection: chromadb.Collection):
    print("\n================== Evaluation ==================\n")
    passed = 0
    for case in TEST_CASES:
        chunks = retrieve(case["question"], collection)
        answer = generate_answer(case["question"], chunks)
        ok = case["expected"].lower() in answer.lower()
        if ok:
            passed += 1
        print(f"Q: {case['question']}")
        print(f"A: {answer}")
        print(f"Expected to contain: '{case['expected']}' → {'PASS' if ok else 'FAIL'}\n")
    print(f"Result: {passed}/{len(TEST_CASES)} passed")


def generate_answer(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "Answer the question using only the context provided. If the answer is not in the context, say you don't know."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )
    return response.message.content or "No response generated"  # Ollama format, not OpenAI


def retrieve(question: str, collection: chromadb.Collection, top_k: int = 3) -> list[str]:
    # Embed the question using the same model
    question_embedding = ollama.embeddings(
        model="nomic-embed-text", prompt=question)["embedding"]

    # Search the vector store
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
    )

    chunks = results["documents"][0] if results["documents"] else []  # list of top-k matching chunks
    for i, chunk in enumerate(chunks):
        print(f"Result {i + 1}:\n{chunk}\n")

    return chunks


def store_in_chroma(chunks: list[str], embeddings: list[list[float]]) -> chromadb.Collection:
    import numpy as np
    client = chromadb.PersistentClient(path=".chroma")  # saves to disk
    collection = client.get_or_create_collection("my_docs")

    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        embeddings=np.array(embeddings),
    )
    print(f"Stored {len(chunks)} chunks in Chroma")

    return collection


def embed_chunks(chunks: list[str]) -> list[list[float]]:
    return [
        ollama.embeddings(model="nomic-embed-text", prompt=chunk)["embedding"]
        for chunk in chunks
    ]


def load_documents() -> str:
    # Load files (PDFs, markdown, .txt) from a local folder
    # Parse raw text out of each file
    docs_path = Path(__file__).parent / "documents"
    content = ""
    for doc in docs_path.glob("*.txt"):
        print(f"Reading document: {doc.name}")
        with open(doc, "r") as f:
            content += f.read()
            print(f"Content of {doc.name}:\n{content}\n")
    return content


def chunk_text(text: str, chunk_size: int = 50, overlap: int = 5) -> list[str]:
    tokens = text.split()  # Simple tokenization by whitespace
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = tokens[i:i + chunk_size]
        chunks.append(" ".join(chunk))

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:\n{chunk}\n")

    return chunks


if __name__ == "__main__":
    main()
