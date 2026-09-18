from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI()

##System Message: It is a message that sets the context for the conversation. It can be used to provide instructions or guidelines to the AI model. It is also know as system prompt. It is used to set the behavior of the AI model. It can be used to provide instructions or guidelines to the AI model. It is also known as system prompt. It is used to set the behavior of the AI model.

##Human Message: It is a message that represents the input from the user. It is used to provide the AI model with the user's input or query. It is also known as user message

##AI Message: It is a message that represents the output from the AI model. It is used to provide the user with the AI model's response or answer. It is also known as assistant message. 


messages=[
    SystemMessage(content='You are a helpful assistant that summarizes research papers.'),
    HumanMessage(content='Tell me about Langchain')
]


result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)