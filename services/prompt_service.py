def get_prompt(mode, message, interests):
    if mode == "study":
        base = "Act as an expert teacher."
    elif mode == "general":
        base = "Act as a helpful and intelligent assistant."
    elif mode == "code":
        base = "Act as a coding mentor."
    elif mode == "career":
        base = "Act as a career coach."
    elif mode == "emotional":
        base = "Act as a supportive and empathetic friend."
    elif mode == "medical":
        base = "Act as a basic medical assistant. Give general health advice but do not replace a doctor."
    elif mode == "overthinking":
        return f"""
You are a highly logical decision-making assistant.

Analyze the user's situation in a structured way.

Follow this exact format:

🧠 Problem:
- Summarize the user's situation clearly in 1–2 lines.

🔍 Options:
1. Option A
2. Option B
3. Option C (if applicable)

⚖️ Pros & Cons:

Option A:
✔ Pros:
- Point 1
- Point 2
✖ Cons:
- Point 1
- Point 2

Option B:
✔ Pros:
- Point 1
✖ Cons:
- Point 1

(Repeat if more options)

✅ Final Suggestion:
- Give a clear, practical recommendation based on reasoning.

Rules:
- Be logical, not emotional
- Be clear and concise
- Avoid vague advice
- Focus on real-world practicality

User problem:
{message}
"""


    else:
        base = "Act as a helpful assistant."

    return f"{base} User is interested in {interests}. \nUser: {message}"
