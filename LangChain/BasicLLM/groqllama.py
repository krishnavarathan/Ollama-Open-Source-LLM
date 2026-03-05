from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model=ChatGroq(model='llama-3.1-8b-instant')

res=model.invoke('Hello. tell about AI in ONe Sentence')
print(res.content)

# a=int(input("Enter the number: "))
# print(a)
