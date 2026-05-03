from pathlib import Path

from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import BaseNode, MetadataMode
from llama_index.embeddings.ollama import OllamaEmbedding


def main():
    # 1. Read the documents with LlamaIndex
    documents = load_documents()
    print(f"Loaded {len(documents)} document(s).")

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

def load_documents() -> list[Document]:
    docs_path = Path(__file__).resolve().parents[1] / "data"
    return SimpleDirectoryReader(str(docs_path)).load_data()


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


if __name__ == "__main__":
    main()
