from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user import router as user_router
from routes.usage import router as usage_router
from routes.chat import router as chat_router

app = FastAPI()

# ✅ CORS MUST BE HERE (RIGHT AFTER app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ THEN ROUTES
app.include_router(user_router)
app.include_router(usage_router)
app.include_router(chat_router)
