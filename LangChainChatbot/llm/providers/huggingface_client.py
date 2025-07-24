# llm/providers/huggingface_client.py

# llm/providers/huggingface_client.py

import os
import logging
from huggingface_hub import InferenceClient
from config.settings import HUGGINGFACE_API_TOKEN, HUGGINGFACE_MODEL_ID

class HuggingFaceClient:
    def __init__(self):
        try:
            self.client = InferenceClient(
                provider="together",
                api_key=HUGGINGFACE_API_TOKEN
            )
        except Exception:
            logging.exception("Failed to initialize HuggingFace InferenceClient")

    def chat(self, messages):
        try:
            # Example: messages = [{"role": "user", "content": "Hello"}]
            response = self.client.chat.completions.create(
                model=HUGGINGFACE_MODEL_ID,
                messages=messages,
                temperature=0.7,
                top_p=0.9,
                max_tokens=300
            )
            return response.choices[0].message.content.strip()
        except Exception:
            logging.exception("Hugging Face chat completion failed")
            return "Sorry, the model could not respond at the moment."
