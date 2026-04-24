import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def get_ai_response(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "qwen/qwen3-next-80b-a3b-instruct:free",
        "messages": messages,
        "temperature": 0.7,
    "max_tokens": 500
    }

    try:
        # 🔹 API call with timeout
        response = requests.post(url, headers=headers, json=data, timeout=10)

        # 🔹 Check response status
        if not response.ok:
            return "AI service unavailable. Try again."

        result = response.json()

        # 🔹 Validate response structure
        if "choices" not in result or len(result["choices"]) == 0:
            return "Sorry, something went wrong. Please try again."

        # 🔹 Extract clean response
        try:
             return result["choices"][0]["message"]    ["content"].strip()
        except:
          return "AI response error. Please try again."

    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."

    except requests.exceptions.RequestException:
        return "Network error. Please check your connection."

    except Exception as e:
        return f"Error: {str(e)}"
    
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

Rules:
- If user is confused or asking for decision → overthinking
- If emotional distress → emotional
- If learning → study
- If job-related → career

ONLY return the mode name. No explanation.

Message:
{message}
"""

    messages = [{"role": "system", "content": prompt}]

    response = get_ai_response(messages)

    return response.strip().lower()


def summarize_chat(history):
    summary_prompt = "Summarize this conversation in 2-3 short simple lines."

    messages = [
        {"role": "system", "content": summary_prompt},
        {"role": "user", "content": str(history)}
    ]

    return get_ai_response(messages)
