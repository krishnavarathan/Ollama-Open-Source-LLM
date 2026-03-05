from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

chat_prompt=ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('You ar a helpful assistent that provides information about {subject}'),
    HumanMessagePromptTemplate.from_template('Can you tell me somthing interesting about {subject}')
])

sub=str(input("Enter the topic: "))
prompt_res =chat_prompt.format_messages(subject=sub)
print(prompt_res)
