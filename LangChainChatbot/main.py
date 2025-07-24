# signature_cafe_chatbot/main.py

import logging
import os
from config import settings

# Configure logging to file
logging.basicConfig(
    filename='chatbot_runtime.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    from ui.chat_ui import launch_chat_ui
    from core.chat_engine import initialize_chat_engine
except ImportError as import_error:
    logging.exception("Failed to import one or more modules. Make sure all dependencies are installed.")
    print("Import error. Please check that all required modules are present and installed.")
    raise import_error

if __name__ == '__main__':
    try:
        # Log non-sensitive environment variables for debugging
        logging.info("Environment configuration:")
        for key, value in os.environ.items():
            if 'KEY' not in key and 'TOKEN' not in key and 'SECRET' not in key:
                logging.info(f"{key} = {value}")

        # Log current config settings from settings.py
        logging.info("Loaded config settings:")
        logging.info(f"LLM_PROVIDER = {settings.LLM_PROVIDER}")
        logging.info(f"MENU_FILE = {settings.MENU_FILE}")
        logging.info(f"DEFAULT_SYSTEM_PROMPT = {settings.DEFAULT_SYSTEM_PROMPT[:50]}...")

        llm_engine = initialize_chat_engine()
        launch_chat_ui(llm_engine)
    except Exception as e:
        logging.exception("An error occurred while starting the chatbot:")
        print("Something went wrong during initialization. Please check chatbot_runtime.log for details.")
