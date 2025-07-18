from fastapi import FastAPI, Depends, HTTPException
from models.request import IntegrationRequest
from auth.security import authorize
from utils.response import normalize_response
from handlers import get_handler

app = FastAPI()

@app.post("/integration/{provider}")
async def integration_handler(provider: str, 
                              request: IntegrationRequest, 
                              auth=Depends(authorize)):
    handler = get_handler(provider)
    if not handler:
        raise HTTPException(status_code=404, detail="Provider not found")

    try:
        result = await handler(request.action, request.parameters)
        return normalize_response(result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Integration failed : {str(e)}")