from fastapi import HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader

API_KEY = "secret-api-key"
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)):
    """
    Dependency to validate the API key from the request header.
    Raises:
        HTTPException: If the API key is invalid or missing.
    """
    if api_key == API_KEY:
        return api_key
    raise HTTPException(status_code=403, detail="Could not validate credentials")