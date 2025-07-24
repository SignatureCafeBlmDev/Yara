import requests
from config.settings import RUNPOD_API_KEY

class RunPodClient:
    def __init__(self):
        self.endpoint = os.getenv("RUNPOD_ENDPOINT_URL")  # You must set this in .env
        self.headers = {
            "Authorization": f"Bearer {RUNPOD_API_KEY}",
            "Content-Type": "application/json"
        }

    def chat(self, messages):
        # Format messages into prompt string (latest only for now)
        user_msg = messages[-1]["content"]

        data = {
            "input": {"prompt": user_msg}
        }

        try:
            response = requests.post(self.endpoint, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("output", "I'm sorry, I didn't understand that.")
        except Exception as e:
            return "Sorry, the RunPod model is currently unavailable. Please try again later."