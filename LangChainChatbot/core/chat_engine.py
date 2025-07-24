# core/chat_engine.py

import logging
from llm.llm_router import get_llm_client
from data.menu_loader import load_menu
from core.prompts import build_messages

MAX_HISTORY = 10

class ChatEngine:
    def __init__(self):
        try:
            self.llm = get_llm_client()
            self.history = []
            self.menu = load_menu()
        except Exception as e:
            logging.exception("Failed to initialize ChatEngine")
            raise e

    def chat(self, user_input):
        try:
            self.history = self.history[-MAX_HISTORY:]
            self.history.append({"role": "user", "content": user_input})
            messages = build_messages(self.history, self.menu)          
            response = self.llm.chat(messages)
            self.history.append({"role": "assistant", "content": response})
            return response

        except Exception as e:
            logging.exception("Error during chat generation")
            return "Sorry, there was a problem processing your request. Please try again."


# ✅ This must be here to avoid ImportError
def initialize_chat_engine():
    return ChatEngine()
