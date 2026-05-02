from pathlib import Path

import ollama


def main():

    # Load documents from the "docs" directory
    content = load_documents()

    # Chunk the text into smaller pieces (e.g. 50 tokens, with overlap)
    chunks = chunk_text(content)
    
    # Embed the chunks using a simple embedding method (e.g. TF-IDF, or a pre-trained model)
    embeddings = embed_chunks(chunks)
    print(f"Embedded {len(embeddings)} chunks, dimension: {len(embeddings[0])}")
    
    
def embed_chunks(chunks: list[str]) -> list[list[float]]:
    return [
        ollama.embeddings(model="nomic-embed-text", prompt=chunk)["embedding"]
        for chunk in chunks
    ]

def load_documents() -> str:
    # Load files (PDFs, markdown, .txt) from a local folder
    # Parse raw text out of each file
    docs_path = Path(__file__).parent / "documents"
    for doc in docs_path.glob("*.txt"):
        print(f"Reading document: {doc.name}")
        with open(doc, "r") as f:
            content = f.read()
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
