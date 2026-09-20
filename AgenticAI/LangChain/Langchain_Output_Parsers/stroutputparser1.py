from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

model=ChatOpenAI()

#1st prompt-> Detailed report
template1=PromptTemplate(
    template='Write a detialed report on {topic}',
    input_variables=['topic']
)

#2nd prompt ->summary
template2=PromptTemplate(
    template='Write a 5 line summary on the following topic. /n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic': 'Black Hole'})

print(result)