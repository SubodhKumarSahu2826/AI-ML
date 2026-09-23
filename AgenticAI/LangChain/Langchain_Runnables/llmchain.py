from langchain_core import PromptTemplate
from langchain_openai import OpenAI
from langchain_classic.chains import LLMChain

# Initialize the LLM
llm=OpenAI(
    model_name='gpt-3.5-turbo', 
    temperature=0.9 
)

#Create a prompt template
prompt=PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}"
)

# Create an LLMChain
chain=LLMChain(llm=llm, prompt=prompt)

#Run the chain with a specific topic
topic=input('Enter a topic')
output=chain.run(topic)

print("Generated Blog Title:", output)