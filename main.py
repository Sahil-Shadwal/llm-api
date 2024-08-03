from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import ollama
import os

app = FastAPI()

# List available models
models = [model["name"] for model in ollama.list()["models"]]

# Ensure the desired model is available
desired_model = "llama3.1:latest"
if desired_model in models:
    MODEL_NAME = desired_model
else:
    raise ValueError(f"Model '{desired_model}' not found. Available models: {models}")

class RequestBody(BaseModel):
    prompt: str

@app.post("/generate/")
async def generate_text(request: RequestBody):
    messages = [{"role": "user", "content": request.prompt}]
    stream = ollama.chat(model=MODEL_NAME, messages=messages, stream=True)
    generated_text = ""
    for chunk in stream:
        generated_text += chunk["message"]["content"]
    return {"generated_text": generated_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)