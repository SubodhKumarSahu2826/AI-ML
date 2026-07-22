from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re

app = FastAPI(
    title="Text Summarizer App",
    description="Text Summarization using T5",
    version="1.0"
)


# Load Model from Hugging Face

MODEL_NAME = "SubodhKumarSahu2826/t5-text-summarizer"

print("Loading model...")

model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)


# Device Configuration

if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)
model.eval()

print(f"Model loaded successfully on {device}")


# Templates

templates = Jinja2Templates(directory="templates")


class DialogueInput(BaseModel):
    dialogue: str


def clean_data(text: str) -> str:
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    return text.strip().lower()


def summarize_dialogue(dialogue: str) -> str:

    dialogue = clean_data(dialogue)

    inputs = tokenizer(
        dialogue,
        max_length=512,
        truncation=True,
        padding="max_length",
        return_tensors="pt"
    ).to(device)

    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=150,
            num_beams=4,
            early_stopping=True
        )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return summary



# API Routes


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):

    if not dialogue_input.dialogue.strip():
        return {"summary": "Please enter some text."}

    summary = summarize_dialogue(dialogue_input.dialogue)

    return {
        "summary": summary
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}