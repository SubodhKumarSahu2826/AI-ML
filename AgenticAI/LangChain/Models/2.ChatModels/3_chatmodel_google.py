from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')

result=model.invoke("Who is known as the God of Cricket?")
print(result.content)