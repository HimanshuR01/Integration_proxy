from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer, HTTPBasicCredentials, HTTPBasic
from typing import Optional


VALID_API_KEYS = {"valid_api_key"} 
VALID_TOKENS = {"valid-oauth-token"}
VALID_USERS = {"user": "pass"}

api_key_scheme = APIKeyHeader(name="X-API-Key", auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
basic_auth = HTTPBasic()

async def authorize(api_key: Optional[str] = Depends(api_key_scheme),
                    oauth_token: Optional[str] = Depends(oauth2_scheme),
                    credentials: Optional[HTTPBasicCredentials] = Depends(basic_auth)):
    if api_key in VALID_API_KEYS:
        return
    if oauth_token in VALID_TOKENS:
        return
    if VALID_USERS.get(credentials.username) == credentials.password:
        return
    raise HTTPException(status_code=401, detail="Unauthorized access")

