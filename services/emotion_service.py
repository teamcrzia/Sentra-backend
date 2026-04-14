def detect_emotion(message):
    msg = message.lower()

    if any(word in msg for word in ["sad", "depressed", "cry", "upset", "lonely"]):
        return "sad"
    elif any(word in msg for word in ["angry", "frustrated", "annoyed"]):
        return "angry"
    elif any(word in msg for word in ["happy", "excited", "great"]):
        return "happy"
    
    return "neutral"


def detect_intent(message):
    msg = message.lower()

    if "how" in msg or "what" in msg or "why" in msg:
        return "question"
    elif "should i" in msg or "can i" in msg:
        return "advice"
    elif "explain" in msg:
        return "explanation"
    
    return "general"
