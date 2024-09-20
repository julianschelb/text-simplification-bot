import gradio as gr
import requests

# Function to send the paragraph to an API and get the simplified response


def simplify_text(paragraph):
    pass
    # API_URL = "https://api-inference.huggingface.co/models/YOUR_MODEL_NAME"  # Replace with your model's API URL
    # headers = {"Authorization": f"Bearer YOUR_HUGGINGFACE_API_KEY"}  # Replace with your Hugging Face API Key

    # # Send request to the API
    # data = {
    #     "inputs": paragraph,
    #     "parameters": {
    #         "max_new_tokens": 50,  # Adjust as needed for response length
    #         "temperature": 0.7      # Adjust for randomness
    #     }
    # }

    # response = requests.post(API_URL, headers=headers, json=data)

    # if response.status_code == 200:
    #     result = response.json()
    #     return result[0]["generated_text"]  # Assuming API returns simplified text here
    # else:
    #     return f"Error: {response.status_code} - {response.text}"

# Create a Gradio interface with a text input and a "Simplify" button


def create_gradio_interface():
    """Create a Gradio interface for the text simplification bot."""

    with gr.Blocks() as app:

        gr.Markdown("## Bitty Bot")
        paragraph_input = gr.Textbox(
            label="Enter your paragraph", placeholder="Type or paste your text here...", lines=5)
        simplify_button = gr.Button("Simplify")
        output = gr.Textbox(label="Simplified Text", lines=5)

        # Define what happens when the button is clicked
        simplify_button.click(
            simplify_text, inputs=paragraph_input, outputs=output)

    return app


# Run the Gradio app
if __name__ == "__main__":
    app = create_gradio_interface()
    app.launch()
