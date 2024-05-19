from fastapi import APIRouter, HTTPException
from ..services.gemini_service import GeminiService

    

router = APIRouter()
gemini_service = GeminiService()


@router.post("/query")
async def query(sentence: str, options: dict):
    print("sentence: ", sentence)
    try:
        # global human_input
        # if human_input: # if human input is not empty, it means our query is a follow-up query to the human input request
        #     human_input = False
        #     return langchain_service.text_to_sql(human_input) 

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
