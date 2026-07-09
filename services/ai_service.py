import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BLUESMINDS_API_KEY")
URL = os.getenv("BLUESMINDS_URL")
MODEL = os.getenv("MODEL_NAME")


def get_ai_response(messages):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": messages
    }

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=120
        )

        if response.status_code != 200:
            return f"Status Code: {response.status_code}\nResponse: {response.text}"

        result = response.json()

        if "choices" not in result or len(result["choices"]) == 0:
            return "Sorry, something went wrong. Please try again."

        return result["choices"][0]["message"]["content"].strip()

    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."

    except requests.exceptions.RequestException as e:
        return f"Network error: {e}"

    except Exception as e:
        return f"Error: {e}"

def detect_mode_using_ai(message):
    prompt = f"""
Classify the user's message into ONE of these modes:
- study
- code
- career
- emotional
- medical
- general
- overthinking
- image

Rules:
- If user wants to generate, create, draw, design or make an image → image
- If user is confused or asking for decision → overthinking
- If emotional distress → emotional
- If learning → study
- If job-related → career

ONLY return the mode name. No explanation.

Message:
{message}
"""

    messages = [
        {"role": "system", "content": prompt}
    ]

    response = get_ai_response(messages)

    return response.strip().lower()


def summarize_chat(history):
    summary_prompt = "Summarize this conversation in 2-3 short simple lines."

    messages = [
        {
            "role": "system",
            "content": summary_prompt
        },
        {
            "role": "user",
            "content": str(history)
        }
    ]

    return get_ai_response(messages)
