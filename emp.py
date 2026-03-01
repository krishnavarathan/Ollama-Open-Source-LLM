from langchain_community.embeddings import OllamaEmbeddings
import warnings
import logging
# To ingore the unwanted log-message
logging.getLogger().setLevel(logging.ERROR)
warnings.filterwarnings('ignore')

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector = embeddings.embed_query("Hello world")
vector_2 = embeddings.embed_query("Hi world")
# print(len(vector))
# print(len(vector_2))

import numpy as np

v1 = np.array(vector)
v2 = np.array(vector_2)

cosine_similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print(v1)
print(v2)
print("Cosine Similarity:", cosine_similarity)