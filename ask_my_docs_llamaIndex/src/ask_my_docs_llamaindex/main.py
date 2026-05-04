from pathlib import Path

import chromadb
from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import BaseNode, MetadataMode
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


def main():
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
