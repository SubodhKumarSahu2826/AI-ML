from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 

llm=HuggingFacePipeline.from_model_id(
    model_id="openai/gpt-oss-20b",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.6,
        max_new_tokens=112
    )
)

model=ChatHuggingFace(llm=llm)
resulty=model.invoke("What is the capital of Chattisghar a state in India? ")

print(result.content)