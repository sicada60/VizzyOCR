import easyocr
from PIL import Image
import numpy as np
import io
import openai
import streamlit as st

# Load API key securely from Streamlit secrets
import openai
import os

openai.api_key = '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'
def extract_text(image_bytes):
    """
    Extract text from an image using EasyOCR.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image_np = np.array(image)

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image_np, detail=0)
    return result

def generate_emotion_reply_llm(text, tone):
    """
    Generate a reply to the given text in the specified emotional tone using OpenAI GPT.
    """
    prompt = f"""You are a helpful assistant that rewrites messages with specific emotional tones.

Original message: "{text}"

Rewrite the message in a {tone.lower()} tone. Make it sound natural and appropriate for real conversation.
"""

    # Generate a response from OpenAI GPT using the newer ChatCompletion method
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ensure you're using the correct model (like gpt-3.5-turbo)
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )

    # Return the assistant's message from the response
    return response['choices'][0]['message']['content']

# Test functions
if __name__ == "__main__":
    # Example text to test the generation function
    text = "I feel bad about the situation."
    tone = "cheerful"

    # Generate emotion-specific response
    reply = generate_emotion_reply_llm(text, tone)
    print(reply)
