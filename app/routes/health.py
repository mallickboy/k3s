from fastapi import APIRouter, Request, HTTPException
from app.services.home import get_home_page

router = APIRouter()

@router.get("/health")
async def health():
    return {
        "status": "ok"
    }