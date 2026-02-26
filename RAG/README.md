<!-- 🚀 RAG with Ollama (Local LLM + Vector DB) -->

This project implements a Retrieval-Augmented Generation (RAG) pipeline using:

Local LLM via Ollama
LangChain
Chroma Vector Database
PDF ingestion and embedding workflow

<!-- It allows users to: -->

Upload a PDF
Extract and chunk text
Generate embeddings
Store embeddings in a vector database
Perform similarity search
Generate context-aware answers using a local LLM

<!-- 🧠 Architecture Overview -->

PDF → Text Extraction → Chunking → Embeddings → Chroma DB
                                        ↓
                                        Retriever
                                        ↓
                                        LLM (Ollama)
                                        ↓
                                        Answer
