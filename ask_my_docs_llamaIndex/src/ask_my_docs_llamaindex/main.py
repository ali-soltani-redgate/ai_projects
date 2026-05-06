from pathlib import Path
import argparse
from typing import Any

import chromadb
from chromadb.api.types import QueryResult
from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import BaseNode, MetadataMode
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ingest and query local documents.")
    parser.add_argument(
        "--mode",
        choices=["ingest", "query", "both"],
        default="both",
        help="Run ingestion, querying, or both.",
    )
    parser.add_argument(
        "--question",
        type=str,
        default="What is this document about?",
        help="Question to query after ingestion or against existing vectors.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=3,
        help="Number of most similar chunks to return.",
    )
    return parser.parse_args()


def main():
    args = get_args()

    if args.mode in {"ingest", "both"}:
        ingest_documents()

    if args.mode in {"query", "both"}:
        results = query_documents(args.question, top_k=args.top_k)
        print_query_results(args.question, results)
    
    
def ingest_documents():
    # 1. Read the documents with LlamaIndex
    documents = load_documents()
    print(f"Loaded {len(documents)} document(s).")
    
    # 1.1 Improve docs by applying transformation (e.g. remove newlines, extra spaces, etc.) - optional but can help with chunking and embedding quality.

    # 2. Chunk the text into smaller pieces (e.g. 50 tokens, with overlap)
    # Each node is one small text segment plus metadata, not a whole file.
    # Metadata can include file name, chunk index, etc. (not used in this example, but can be helpful for retrieval and debugging). 
    nodes = chunk_documents(documents, chunk_size=50, chunk_overlap=5)
    print(f"Created {len(nodes)} chunk(s).")

    # 3. Embed the chunks using LlamaIndex embedding method
    embeddings = embed_nodes_with_local_model(nodes)
    if embeddings:
        print(
            f"Generated {len(embeddings)} embedding(s), each with {len(embeddings[0])} dimensions."
        )

    # 4. Store the embeddings in a vector database with LlamaIndex (e.g. chromadb)
    vector_count = store_nodes_in_chroma(nodes, embeddings)
    print(f"Stored {vector_count} chunk(s) in the Chroma vector store.")


def query_documents(question: str, top_k: int = 3) -> list[tuple[str, float, dict[str, Any]]]:
    def load_collection() -> chromadb.Collection:
        persist_dir = Path(__file__).resolve().parents[1] / "storage" / "chroma"
        client = chromadb.PersistentClient(path=str(persist_dir))
        return client.get_or_create_collection("ask_my_docs")

    def build_query_embedding(user_question: str) -> list[float]:
        embed_model = OllamaEmbedding(
            model_name="nomic-embed-text",
            base_url="http://localhost:11434",
        )
        return embed_model.get_query_embedding(user_question)

    def run_vector_search(
        collection: chromadb.Collection,
        embedding: list[float],
        k: int,
    ) -> QueryResult:
        return collection.query(
            query_embeddings=[embedding],
            n_results=k,
            include=["documents", "distances", "metadatas"],
        )

    def normalize_results(search_results: QueryResult) -> list[tuple[str, float, dict[str, Any]]]:
        documents_batch = search_results.get("documents") or [[]]
        distances_batch = search_results.get("distances") or [[]]
        metadatas_batch = search_results.get("metadatas") or [[]]

        documents = documents_batch[0] if documents_batch else []
        distances = distances_batch[0] if distances_batch else []
        metadatas = metadatas_batch[0] if metadatas_batch else []

        ranked_results: list[tuple[str, float, dict[str, Any]]] = []
        for doc, distance, metadata in zip(documents, distances, metadatas, strict=True):
            ranked_results.append((str(doc) if doc else "", float(distance), dict(metadata or {})))
        return ranked_results

    collection = load_collection()
    if collection.count() == 0:
        print("No vectors found. Run ingestion first with --mode ingest.")
        return []

    query_embedding = build_query_embedding(question)
    search_results = run_vector_search(collection, query_embedding, top_k)
    return normalize_results(search_results)


def print_query_results(question: str, results: list[tuple[str, float, dict[str, Any]]]) -> None:
    print("\n================== Query ==================")
    print(f"Question: {question}")

    if not results:
        print("No matching chunks found.")
        return

    for idx, (document, distance, metadata) in enumerate(results, start=1):
        source = metadata.get("file_name") or metadata.get("file_path") or "unknown"
        print(f"\nResult {idx}")
        print(f"Distance: {distance:.4f} (lower is better)")
        print(f"Source: {source}")
        print(f"Content: {document[:300]}...")
    

def load_documents() -> list[Document]:
    data_dir = Path(__file__).resolve().parents[1] / "data"
    docs = SimpleDirectoryReader(input_dir=str(data_dir)).load_data()
    print("Documents loaded from data directory:")
    for doc in docs:
        print(f"- {doc.get_content(metadata_mode=MetadataMode.NONE)[:100]}...")  # Print first 100 characters
        # Metadata includes file name, file path, file size, etc.
        print(f"  \n ============= Metadata: \n {doc.metadata}") 
        print(f"  \n ============= Excluded for Embeddings: \n {doc.excluded_embed_metadata_keys}")
        print(f"  \n ============= Excluded for LLM: \n {doc.excluded_llm_metadata_keys}")
        print(f"  \n ============= Excluded for Embeddings: \n {doc.get_content(metadata_mode=MetadataMode.EMBED)}")  # Print content without metadata   
        print(f"  \n ============= Excluded for LLM: \n {doc.get_content(metadata_mode=MetadataMode.LLM)}")  # Print content without metadata
        
    return docs


def chunk_documents(
    documents: list[Document], chunk_size: int, chunk_overlap: int
) -> list[BaseNode]:
    splitter = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.get_nodes_from_documents(documents)


def embed_nodes_with_local_model(nodes: list[BaseNode]) -> list[list[float]]:
    texts = [node.get_content(metadata_mode=MetadataMode.NONE) for node in nodes]
    embed_model = OllamaEmbedding(
        model_name="nomic-embed-text",
        base_url="http://localhost:11434",
    )
    return embed_model.get_text_embedding_batch(texts)


def store_nodes_in_chroma(nodes: list[BaseNode], embeddings: list[list[float]]) -> int:
    persist_dir = Path(__file__).resolve().parents[1] / "storage" / "chroma"
    client = chromadb.PersistentClient(path=str(persist_dir))
    collection = client.get_or_create_collection("ask_my_docs")

    for node, embedding in zip(nodes, embeddings, strict=True):
        node.embedding = embedding

    vector_store = ChromaVectorStore(chroma_collection=collection)
    vector_store.add(nodes)
    return collection.count()


if __name__ == "__main__":
    main()
