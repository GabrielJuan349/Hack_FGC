import logging

from fastapi import FastAPI
from pydantic import BaseModel

from speaker_diarization import SpeakerDiarization

logging.basicConfig(level=logging.INFO)
app = FastAPI()


class Request(BaseModel):
    audio: str | None = None
    frame: str
    location: str
    options: object | None = None


class Response(BaseModel):
    audio: str | None = None
    action: str
    options: object | None = None


@app.get("/")
async def read_root():
    return {"status": "Server is running successfully!"}


@app.get("/call_gemini")
async def read_item(model: Request) -> Response:
    most_relevant_speaker = SpeakerDiarization(model.audio).diarization()
    return Response(
        audio="BASE64_ENCODED_AUDIO",
        action="go_to_payment"
    )
