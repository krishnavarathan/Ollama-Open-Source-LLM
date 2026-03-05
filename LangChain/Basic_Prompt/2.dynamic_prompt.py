from langchain_core.prompts import PromptTemplate

dynamic_prompt = PromptTemplate(
    template='Write a short paragraph about {topic} in {style} style',
    input_variable=['topic', 'style']
)

a=str(input("Enter the Topic: "))
b=str(input("Enter the style: "))
res=dynamic_prompt.format(topic=a, style=b)
print(res)