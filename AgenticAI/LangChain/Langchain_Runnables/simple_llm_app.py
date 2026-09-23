from langchain_core import PromptTemplate
from langchain_openai import OpenAI

# Initialize the LLM
llm=OpenAI(
    model_name='gpt-3.5-turbo', 
    temperature=0.9
)

#Create a prompt template
prompt=PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchu blog title about {topic}"
)

# Define the input
topic=input('Enter a topic')

# Format the prompt manually using PrompTemplate
formatted_prompt=prompt.format(topic=topic)

# Call the LLM directly
blog_title=llm.predict(formatted_prompt)

# Print the output
print("Generated Blog Title:", blog_title)