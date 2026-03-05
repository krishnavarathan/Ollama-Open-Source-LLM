from langchain_core.prompts import PromptTemplate

temp = PromptTemplate(
    input_Variables=[],
    template="write a short fun about AI"
)

promt_text = temp.format()
print(promt_text)