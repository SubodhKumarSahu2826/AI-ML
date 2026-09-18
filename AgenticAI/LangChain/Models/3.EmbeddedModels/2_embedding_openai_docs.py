from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents=[
    "Delhi is the capital of India.",
    "Mumbai is the captial of Maharahstra",
    "Berlin is the capital of Germany."
]

result=embedding.embed_query("delhi is the capital of India.")
print(str(result)) 