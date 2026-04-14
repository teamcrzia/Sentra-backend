from fastapi import APIRouter, Request
from datetime import date
from database import usage
from auth import verify_token

router = APIRouter()


# 🔥 CHECK LIMIT
@router.post("/check-limit")
async def check_limit(req: Request):
    try:
        auth_header = req.headers.get("Authorization")

        if not auth_header:
            return {"error": "No token provided"}

        token = auth_header.split(" ")[1]

        # ✅ GET USER ID FROM FIREBASE
        user_id = verify_token(token)

        today = str(date.today())

        record = usage.find_one({
            "user_id": user_id,
            "date": today
        })

        if record and record["count"] >= 3:
            return {"allowed": False}

        return {"allowed": True}

    except Exception as e:
        return {"error": str(e)}


# 🔥 UPDATE USAGE
@router.post("/update-usage")
async def update_usage(req: Request):
    try:
        auth_header = req.headers.get("Authorization")

        if not auth_header:
            return {"error": "No token provided"}

        token = auth_header.split(" ")[1]

        # ✅ GET USER ID FROM FIREBASE
        user_id = verify_token(token)

        today = str(date.today())

        record = usage.find_one({
            "user_id": user_id,
            "date": today
        })

        if record:
            usage.update_one(
                {"_id": record["_id"]},
                {"$inc": {"count": 1}}
            )
        else:
            usage.insert_one({
                "user_id": user_id,
                "date": today,
                "count": 1
            })

        return {"message": "Usage updated"}

    except Exception as e:
        return {"error": str(e)}
