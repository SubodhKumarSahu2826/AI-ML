from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS


# Load the documents
loader = TextLoader("doc.text")
documents = loader.load()


# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)


# Convert text into embeddings & store in FAISS
vectorstore = FAISS.from_documents(
    docs,
    OpenAIEmbeddings()
)


# Create a retriever
retriever = vectorstore.as_retriever()


# Manually retrieve relevant documents
query = "What are the key takeaways from the documents?"

retrieved_docs = retriever.invoke(query)


# Combine retrieved text into a single prompt
retrieved_text = "\n".join(
    [doc.page_content for doc in retrieved_docs]
)


# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.9
)


# Manually pass retrieved text to LLM
prompt = f"""
Based on the following text, answer the question:

Question:
{query}

Context:
{retrieved_text}
"""

answer = llm.invoke(prompt)


# Print the answer
print("Answer:", answer.content)