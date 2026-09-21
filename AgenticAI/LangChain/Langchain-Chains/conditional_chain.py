from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Model
model = ChatOpenAI()

# Normal string output parser
parser = StrOutputParser()


# Pydantic output schema
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )


# Pydantic parser
parser2 = PydanticOutputParser(pydantic_object=Feedback)


# -------------------------
# Sentiment Classification
# -------------------------

prompt1 = PromptTemplate(
    template=(
        "Classify the sentiment of the following feedback text "
        "into positive or negative.\n"
        "{feedback}\n\n"
        "{format_instruction}"
    ),
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": parser2.get_format_instructions()
    }
)

classifier_chain = prompt1 | model | parser2


# -------------------------
# Positive Response
# -------------------------

prompt2 = PromptTemplate(
    template=(
        "Write an appropriate response to this positive feedback:\n"
        "{feedback}"
    ),
    input_variables=["feedback"]
)


# -------------------------
# Negative Response
# -------------------------

prompt3 = PromptTemplate(
    template=(
        "Write an appropriate response to this negative feedback:\n"
        "{feedback}"
    ),
    input_variables=["feedback"]
)


# -------------------------
# Branching
# -------------------------

branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "positive",
        prompt2 | model | parser
    ),
    (
        lambda x: x.sentiment == "negative",
        prompt3 | model | parser
    ),
    RunnableLambda(lambda x: "Could not find sentiment")
)


# -------------------------
# Final Chain
# -------------------------

chain = classifier_chain | branch_chain


# -------------------------
# Run
# -------------------------

result = chain.invoke({
    "feedback": "This is a beautiful phone"
})

print(result)


# # Display chain graph
# chain.get_graph().print_ascii()