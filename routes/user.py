from fastapi import APIRouter, Request
from database import users
from auth import verify_token

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Backend working"}


@router.post("/verify")
async def verify(req: Request):
    try:
        auth_header = req.headers.get("Authorization")

        if not auth_header:
            return {"error": "No token provided"}

        token = auth_header.split(" ")[1]

        user_id = verify_token(token)

        return {"user_id": user_id}

    except Exception as e:
        return {"error": str(e)}


@router.get("/test-db")
def test_db():
    try:
        users.insert_one({
            "name": "test user",
            "role": "student"
        })
        return {"message": "Inserted into DB"}

    except Exception as e:
        return {"error": str(e)}


@router.post("/save-profile")
async def save_profile(req: Request):
    try:
        auth_header = req.headers.get("Authorization")

        if not auth_header:
            return {"error": "No token provided"}

        token = auth_header.split(" ")[1]
        user_id = verify_token(token)

        data = await req.json()

        users.update_one(
            {"user_id": user_id},   # 🔥 match user
            {
                "$set": {
                    "user_id": user_id,
                    "name": data.get("name"),
                    "dob": data.get("dob"),
                    "role": data.get("role")
                }
            },
            upsert=True  # 🔥 create if not exists
        )

        return {"message": "Profile saved", "user_id": user_id}

    except Exception as e:
        return {"error": str(e)}
    
@router.get("/check-user")
async def check_user(req: Request):
    try:
        auth_header = req.headers.get("Authorization")

        if not auth_header:
            return {"exists": False}

        token = auth_header.split(" ")[1]
        user_id = verify_token(token)

        print("CHECK USER ID:", user_id)  # 🔥 DEBUG

        user = users.find_one({"user_id": user_id})

        print("FOUND USER:", user)  # 🔥 DEBUG

        return {"exists": user is not None}

    except Exception as e:
        print("ERROR:", e)
        return {"exists": False}
