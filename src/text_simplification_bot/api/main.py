from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from huggingface_hub import InferenceClient

app = FastAPI()


@app.post("/simplify_input")
async def simplify_input(request: Request):

    # Parse the JSON data from the request body
    req_data = await request.json()

    # Extract the sentence or input from the JSON dict
    if "complex_sentence" not in req_data:
        return JSONResponse(status_code=400, content={"error": "Missing 'complex_sentence' in the request body"})

    client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta")

    chat_prompt = [
        {"role": "system", "content": "Simplify and shorten sentences for non-native English speakers. Provide a brief, concise summary of the input."},
        {"role": "user",
            "content": f"Simplify this sentence: {req_data.get('complex_sentence')}"}
    ]

    response = client.chat.completions.create(
        messages=chat_prompt, max_tokens=100)

    return {"simplified_sentence": response}
