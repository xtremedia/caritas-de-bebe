import openai
import os
from PIL import Image
import requests
from io import BytesIO

# Ensure you have the OpenAI library installed: pip install openai
# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

def edit_image_with_prompt(image_path, prompt):
    """
    Edit an image based on a textual prompt using OpenAI's DALL-E 2.

    Parameters:
    - image_path: Path to the input image.
    - prompt: Textual description of the desired edit.
    """
    # Load the image and convert it to the format expected by the API
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    
    # Convert image data to a format suitable for the API
    image_b64 = base64.b64encode(image_data).decode('utf-8')
    
    # Make the API call to OpenAI's DALL-E 2
    response = openai.Image.edit(
        image=image_b64,
        prompt=prompt,
    )
    
    # The response contains a URL to the edited image; we download and display it
    image_url = response['data']['url']
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()

# Example usage
image_path = "path/to/your/image.jpg"
prompt = "A description of how you want to edit the image"
edit_image_with_prompt(image_path, prompt)
