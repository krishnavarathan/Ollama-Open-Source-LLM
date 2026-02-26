import ollama

res = ollama.list()

# print(res)

chat = ollama.chat(
    model= 'llama3.2',
    messages=[
        { 'role':'user', 'content':'why sky is blue'}
    ],
    stream=True
)


# ==================================================================================
# ==== The Ollama Python library's API is designed around the Ollama REST API ====
# ==================================================================================


# Generate a new model with modified file name

res = ollama.generate(
    model="ocean_model", 
    prompt="why is the ocean so salty?", 
    stream=True
)
# print(res['message'], end="", flush=True)

for chunk in res:
    print(chunk["response"], end="", flush=True)

# ===================
# -- delete model ---
#=====================

# ollama.delete("ocean_model")

