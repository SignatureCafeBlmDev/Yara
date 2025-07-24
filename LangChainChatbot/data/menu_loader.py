import json
import os
from config.settings import MENU_FILE


def load_menu():
    if not os.path.exists(MENU_FILE):
        raise FileNotFoundError(f"Menu file not found at: {MENU_FILE}")
    try:
        with open(MENU_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "categories" not in data or "ingredients" not in data:
                raise ValueError("Invalid menu file format: missing required sections.")
            return data
    except (json.JSONDecodeError, ValueError) as e:
        raise RuntimeError(f"Failed to load or parse menu file: {e}")
