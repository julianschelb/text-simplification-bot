import gradio as gr
import requests

# Function to send the paragraph to an API and get the simplified response


import requests

def request_simplified_input(input_text: str):
    """
    Sends a POST request to the /simplify_input API endpoint and returns the simplified response.

    Parameters:
        input_text (str): The text that needs to be simplified.
        api_url (str): The base URL of the API (e.g., "http://localhost:8000").

    Returns:
        dict: The API response containing the simplified text.
    """
    api_base_url = "http://127.0.0.1:8000" 
    endpoint = f"{api_base_url}/simplify_input"
    
    # Send a POST request to the API
    try:
        response = requests.post(endpoint, json={"complex_sentence": input_text})
        response.raise_for_status()  # Raises an exception for 4xx/5xx errors
        response_data = response.json()
        # Return the simplified text from the response
        return response_data.get("simplified_sentence").get("choices")[0].get("message").get("content")
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def create_gradio_interface():
    """Create a Gradio interface for the text simplification bot."""


    with gr.Blocks() as app:

        example_sentence = "While the intricacies of quantum computing continue to elude even the most brilliant minds, the rapid advancements in this enigmatic field suggest that we are on the precipice of a technological revolution that, if realized, could redefine the very nature of computation itself, unlocking capabilities that would render current encryption protocols obsolete, revolutionize artificial intelligence, and potentially lead to breakthroughs in material sciences, all of which are as awe-inspiring as they are fraught with ethical and societal implications that must be carefully considered before widespread adoption."
    
        gr.Markdown("## Bitty Bot")
        paragraph_input = gr.Textbox(value=example_sentence,
            label="Enter your paragraph", placeholder="Type or paste your text here...", lines=5)
        simplify_button = gr.Button("Simplify")
        output = gr.Textbox(label="Simplified Text", lines=5, show_copy_button=True)

        # Define what happens when the button is clicked
        simplify_button.click(
            request_simplified_input, inputs=paragraph_input, outputs=output)

    return app


# Run the Gradio app
if __name__ == "__main__":
    app = create_gradio_interface()
    app.launch()
