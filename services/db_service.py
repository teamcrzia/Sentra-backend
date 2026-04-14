from pymongo import MongoClient
from datetime import datetime
from config import Config

# 🔌 Connect to MongoDB
client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]

# Collections
chat_collection = db["chats"]
profile_collection = db["profiles"]
summary_collection = db["summaries"]


# ✅ Get chat history
def get_chat_history(user_id):
    chats = list(
        chat_collection.find({"user_id": user_id})
        .sort("timestamp", -1)
        .limit(10)
    )

    chats.reverse()  # oldest → newest

    # 🔧 Fix Mongo ObjectId for JSON
    for chat in chats:
        chat["_id"] = str(chat["_id"])

    return chats


# ✅ Save chat
def save_chat(user_id, message, response, mode):
    chat = {
        "user_id": user_id,
        "message": message,
        "response": response,
        "mode": mode,
        "timestamp": datetime.utcnow()
    }

    chat_collection.insert_one(chat)


# ✅ Get user profile
def get_user_profile(user_id):
    profile = profile_collection.find_one({"user_id": user_id})

    if not profile:
        # fallback (same behavior as your mock)
        return {
            "user_id": user_id,
            "interests": "technology, coding"
        }

    profile["_id"] = str(profile["_id"])
    return profile


# ✅ Save / update user profile
def save_user_profile(user_id, name, role, interests):
    profile_collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "name": name,
                "role": role,
                "interests": interests
            }
        },
        upsert=True
    )


# ✅ Get summary
def get_summary(user_id):
    data = summary_collection.find_one({"user_id": user_id})

    if not data:
        return ""

    return data.get("summary", "")


# ✅ Save summary
def save_summary(user_id, summary):
    summary_collection.update_one(
        {"user_id": user_id},
        {"$set": {"summary": summary}},
        upsert=True
    )
