import logging

from fastapi import FastAPI
from pydantic import BaseModel

from speaker_diarization import SpeakerDiarization

logging.basicConfig(level=logging.INFO)
app = FastAPI()


class Model(BaseModel):
    audio: str


@app.get("/")
async def read_root():
    return {"status": "Server is running successfully!"}


@app.get("/speaker_diarization")
async def read_item(model: Model):
    most_relevant_speaker = SpeakerDiarization(model.audio).diarization()
    return {"most_relevant_speaker": most_relevant_speaker}
