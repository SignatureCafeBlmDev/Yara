import openai
from config.settings import OPENAI_API_KEY, DEFAULT_SYSTEM_PROMPT

class OpenAIClient:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def chat(self, messages):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or gpt-3.5-turbo
                messages=messages,
                temperature=0.4,
                max_tokens=600,
                timeout=10
            )
            return response['choices'][0]['message']['content'].strip()
        except openai.error.OpenAIError as e:
            return "Sorry, I'm having trouble reaching the assistant right now. Please try again shortly."
        except Exception as e:
            return "An unexpected error occurred while processing your request."