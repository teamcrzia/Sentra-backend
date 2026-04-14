from fastapi import APIRouter
from pydantic import BaseModel

from services.ai_service import get_ai_response, summarize_chat, detect_mode_using_ai
from services.prompt_service import get_prompt
from services.emotion_service import detect_emotion, detect_intent
from services.db_service import (
    get_chat_history,
    get_user_profile,
    save_chat,
    get_summary,
    save_summary
)

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: str
    mode: str | None = None
    disappearing: bool = False


@router.post("/chat")
def chat(req: ChatRequest):
    try:
        message = req.message
        mode = req.mode
        user_id = req.user_id
        is_disappearing = req.disappearing

        msg_lower = message.lower()

        # 🔹 Mode detection
        if not mode:
            try:
                mode = detect_mode_using_ai(message)
            except:
                if any(x in msg_lower for x in ["confused", "should i"]):
                    mode = "overthinking"
                elif any(x in msg_lower for x in ["sad", "depressed"]):
                    mode = "emotional"
                elif any(x in msg_lower for x in ["fever", "pain"]):
                    mode = "medical"
                elif any(x in msg_lower for x in ["code", "bug"]):
                    mode = "code"
                elif any(x in msg_lower for x in ["study", "exam"]):
                    mode = "study"
                elif any(x in msg_lower for x in ["job", "career"]):
                    mode = "career"
                else:
                    mode = "general"

        VALID_MODES = ["study", "code", "career", "emotional", "medical", "general", "overthinking"]
        if mode not in VALID_MODES:
            mode = "general"

        # 🔹 Emotion + Intent
        emotion = detect_emotion(message)
        intent = detect_intent(message)

        # 🔹 Profile
        profile = get_user_profile(user_id) or {}
        interests = profile.get("interests", "general")

        # 🔹 Prompt
        prompt = get_prompt(mode, message, interests)

        # 🔹 History
        history = get_chat_history(user_id) or []

        # 🔹 Summary
        summary = get_summary(user_id)

        messages = [{"role": "system", "content": prompt}]

        if summary:
            messages.append({"role": "system", "content": summary})

        for chat in history[-5:]:
            messages.append({"role": "user", "content": chat["message"]})
            messages.append({"role": "assistant", "content": chat["response"]})

        messages.append({"role": "user", "content": message})

        # 🔥 AI call
        response = get_ai_response(messages)

        if not response:
            response = "Sorry, I couldn't process that."

        if not is_disappearing:
            save_chat(user_id, message, response, mode)

        return {
            "success": True,
            "data": {
                "response": response.strip(),
                "mode": mode
            }
        }

    except Exception as e:
        return {"success": False, "error": str(e)}


@router.get("/get-chats/{user_id}")
def get_chats(user_id: str):
    chats = get_chat_history(user_id) or []
    return {"success": True, "data": chats}
