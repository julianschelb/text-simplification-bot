from fastapi import FastAPI
from huggingface_hub import InferenceApi, InferenceClient

app = FastAPI()



@app.post("/simplify_input")
async def simplify_input(request):
    client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta")
    
    chat_prompt = [
        {"role":"system", "content":"Be a helpful assistant by simplifying sentences for non-native speakers of English."},
        {"role":"user", "content": request}
    ]
    
    response = client.chat.completions.create(messages=chat_prompt, max_tokens=100)
    
    return {"simple": response}