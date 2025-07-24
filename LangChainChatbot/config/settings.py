# config/settings.py

import os
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

# === LLM PROVIDER OPTIONS ===
# Options: openai, huggingface, runpod
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "")

# === API Keys ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN", "")
RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY", "")

# === Model IDs ===
HUGGINGFACE_MODEL_ID = os.getenv("HUGGINGFACE_MODEL_ID", "")
HUGGINGFACE_PROVIDER = os.getenv("HUGGINGFACE_PROVIDER", "")

# === Menu & Prompt ===
MENU_FILE = os.getenv("MENU_FILE", "")

DEFAULT_SYSTEM_PROMPT = (
    "You are a helpful nutritionist at Signature Cafe. "
    "You ONLY answer questions related to the menu, food items, ingredients, and dietary goals. "
    "Do NOT answer anything outside this scope. If asked about non-menu topics, kindly refuse and steer the user back to food-related topics."
)
#print("HF TOKEN (preview):", HUGGINGFACE_API_TOKEN[:10])
