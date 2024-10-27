import time

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from app import livepeer_swarm


load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        if request.prompt.lower() == "exit":
            return {"response": "Hope you're enjoy, see you!"}
        video_id = await livepeer_swarm.chat(request.prompt)
        return {"video_id": video_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

