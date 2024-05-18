import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from classes.speaker_diarization import SpeakerDiarization
from ai.app.services.tts.transform_Text_Speech import speech_to_text

from ai.app.api.routes import router
from ai.app.services.gemini_service import GeminiService



logging.basicConfig(level=logging.INFO)
app = FastAPI()
# app.include_router(router)

gemini_service = GeminiService()



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

import requests

@app.get("/call_gemini")
async def read_item(model: Request) -> Response:
    diarization = SpeakerDiarization(model.audio).diarization()
    if diarization is None:
        return Response(action="error", options=None)
    
    text = speech_to_text(diarization.get("audio"))

    print("text", text)

    response = gemini_service.text_to_sql(text, model.options)
        
    print(response)

    return response


@router.post("/query")
async def query(sentence: str, options: dict):
    print("sentence: ", sentence)
    try:
        response = gemini_service.text_to_sql(sentence, options)
        
        print(response)

        return response
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/poke")
async def poke_llm(options: dict):
    try:
        response = gemini_service.initial_poke(options)

        print(response)
        
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)