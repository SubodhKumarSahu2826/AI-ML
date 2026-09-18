from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents=[
    "Virat Kohili is an Indian cricker known for hsi aggresive batting and leadership skills.",
    "MS Dhoni is a former Indian cricker faamous for his calm demeanor and finishing abilities.",
    "Sachin Tendulkar, also know as the 'God of Cricket', is one of the greatest batsmen in the history of cricket."
    "Rohit Sharma is know for his elegant batting and record breaking double centuries in One Day Internationals.",
    "Jasprit Bumrah us an Indian fast bowler known for his unorthodox action and deadly yorkers."
]

query='Who is known for his yorkers?'

doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding], doc_embeddings)[0]

index, score=(sorted(list(enumerate(scores)), key=lambda x:x[1])[-1])

print(query)
print(documents[index])
print("Similarity Score:", score)