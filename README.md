# 🤖 AI Chat Backend (Flask)

## 📌 Overview
This project is a modular AI-powered chat backend built using Flask.  
It supports multiple conversation modes, emotion-aware responses, and context-based memory to deliver intelligent and personalized conversations.

---

## 🚀 Features

- 🔹 Mode-based AI responses  
  (study, code, career, emotional, medical, general)

- 🔹 Emotion Detection  
  Detects user mood (sad, angry, happy, neutral) and adapts responses

- 🔹 Intent Detection  
  Identifies user intent (question, advice, explanation)

- 🔹 Smart Memory System  
  Uses recent chat history + AI-generated summaries for context

- 🔹 Disappearing Messages  
  Emotional chats are not stored (privacy-focused)

- 🔹 Modular Architecture  
  Clean service-based design for scalability and easy integration

- 🔹 AI Integration  
  Uses DeepSeek via OpenRouter for generating responses

- 🧠 Overthinking Mode  
  Helps users make decisions by breaking problems into structured analysis:
  - Problem summary  
  - Options  
  - Pros & Cons  
  - Clear final suggestion  
---

- 🧠 Overthinking → Structured decision-making assistant  

## 🏗️ Project Structure
ai-chat-backend/
│
├── app.py # Main Flask API
│
├── services/
│ ├── ai_service.py # AI integration (DeepSeek/OpenRouter)
│ ├── prompt_service.py # Mode-based prompt generation
│ ├── emotion_service.py # Emotion + intent detection
│ ├── db_service.py # Mock DB (future API integration)
│
├── .env # API keys
├── requirements.txt # Dependencies
├── README.md # Project documentation


---

## ⚙️ Architecture

User (Frontend)
↓
Flask API (app.py)
↓
Emotion + Intent Detection
↓
Prompt Engineering System
↓
Memory Layer (history + summary)
↓
AI Service (DeepSeek via OpenRouter)
↓
Database Layer (Mock / Future API)

---

## 📡 API Endpoint

### 🔹 POST /chat

#### Request:
```json
{
  "message": "Explain recursion",
  "mode": "study",
  "user_id": "1"
}

Response:
{
  "status": "success",
  "data": {
    "response": response.strip(),
    "disappearing": is_disappearing
  }
}

Setup Instructions
git clone <your-repo-link>
cd ai-chat-backend

pip install -r requirements.txt

python app.py