
Project 1 — "Ask My Docs" RAG Chatbot
Here's the high-level implementation flow:

1. Ingest Documents
Load files (PDFs, markdown, .txt) from a local folder
Parse raw text out of each file
Chunk the text into smaller pieces (e.g. 500 tokens, with overlap)
2. Embed & Store
Run each chunk through an embedding model (e.g. text-embedding-3-small via OpenAI, or a local model via Ollama)
Store the vectors in a vector database (e.g. Chroma, FAISS, or Qdrant)
3. Retrieval Pipeline
Take the user's question → embed it
Run a similarity search against the vector DB → get top-k relevant chunks
Optionally combine with keyword search (hybrid search)
4. Generate Answer
Build a prompt: "Answer the question using only the context below: {chunks} \n\nQuestion: {question}"
Send to an LLM (OpenAI, Anthropic, or local via Ollama)
Stream the response back to the user
5. Evaluate
Test with known Q&A pairs
Measure faithfulness (is the answer grounded in the docs?) and relevance (did retrieval surface the right chunks?)

Suggested Stack (simple start)
Component	Tool
Orchestration	LangChain or plain Python
Embeddings	OpenAI or sentence-transformers
Vector DB	Chroma (local, zero-config)
LLM	OpenAI GPT-4o or Ollama (local)
UI	Streamlit or CLI
