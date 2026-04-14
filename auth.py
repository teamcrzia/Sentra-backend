import os
import firebase_admin
from firebase_admin import credentials, auth

# Get current file directory (backend folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct path
cred_path = os.path.join(BASE_DIR, "crezia-mira-ai-firebase-adminsdk-fbsvc-382f1ab24f.json")

cred = credentials.Certificate(json.loads(os.environ.get("FIREBASE_CREDENTIALS")))

# Prevent duplicate initialization
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)


def verify_token(id_token):
    try:
        decoded = auth.verify_id_token(id_token)
        print("✅ TOKEN OK:", decoded)
        return decoded["uid"]
    except Exception as e:
        print("❌ TOKEN ERROR:", e)
        raise e
