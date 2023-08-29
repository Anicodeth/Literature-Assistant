from litassist.services.ai_services.literature_service import LitService
from litassist.configurations.api_configuration import router

lit_service = LitService()

@router.get('/poem/{prompt}')
def get_poem(prompt:str):
    return lit_service.get_poem(prompt)

@router.get('/story/{prompt}')
def get_story(prompt:str):
    return lit_service.get_story(prompt)
