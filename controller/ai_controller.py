from ..services.ai_services.literature_service import LitService
from ..configurations.api_configuration import router
from fastapi import APIRouter

lit_service = LitService()

@router.get('/ai/poem')
def get_poem(prompt: str):
    return lit_service.get_poem(prompt)
