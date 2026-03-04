📚 Semantic Book Recommendation System

A Semantic Book Recommendation System built using Python, NLP, Vector Search, and Gradio.
This project recommends books based on the meaning of a user's query rather than exact keyword matching.

The system uses semantic search with embeddings, text classification, and sentiment/emotion analysis to provide intelligent book recommendations.

🚀 Project Overview

Traditional search systems rely on keyword matching, which often fails to understand the real intent of the user.
This project implements semantic search that understands the context and meaning of queries.

For example:

User Query:
Educational book that explains artificial intelligence for children
The system can recommend books related to AI, machine learning, or beginner AI concepts for kids, even if the exact words do not match.

🧠 Features

Semantic book search using vector embeddings
Vector database for fast similarity search
Text classification for book categories
Emotion / sentiment analysis of book descriptions
Interactive recommendation dashboard built with Gradio
Book filtering by category and emotional tone

📄Notebooks

data-extraction.ipynb
Extracts and cleans raw book data.

text-classification.ipynb
Implements NLP classification for book categories.

text-classification-1.ipynb
Additional classification experiments.

sentiment-analysis.ipynb
Analyzes emotions and sentiments in book descriptions.

vector-search.ipynb
Creates embeddings and builds the semantic vector search system.

Application

gradio-dashboard.py
Main application file that launches the Gradio dashboard for interactive book recommendations.
