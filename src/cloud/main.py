import logging

from fastapi import FastAPI
from pydantic import BaseModel

from classes.speaker_diarization import SpeakerDiarization
from ai.app.services.tts.transform_Text_Speech import speech_to_text

from ai.app.api.routes import router



logging.basicConfig(level=logging.INFO)
app = FastAPI()
app.include_router(router)




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
    diarization = SpeakerDiarization(model.audio).diarization()
    text = speech_to_text(diarization.get("audio"))

    return Response(
        audio="BASE64_ENCODED_AUDIO",
        action="go_to_payment",
        options={"text": text}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)