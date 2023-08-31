from litassist.services.ai_services.literature_service import LitService
from litassist.configurations.api_configuration import router

lit_service = LitService()

@router.get('/poem/{prompt}')
def get_poem(prompt:str):
    return lit_service.get_poem(prompt)

@router.get('/story/{prompt}')
def get_story(prompt:str):
    return lit_service.get_story(prompt)

@router.get('/essay/{prompt}')
def get_essay(prompt:str):
    return lit_service.get_essay(prompt)

@router.get('/fiction/{prompt}')
def get_fiction(prompt:str):
    return lit_service.get_fiction(prompt)

@router.get('/lyrics/{prompt}')
def get_lyric(prompt:str):
    return lit_service.get_lyrics(prompt)

@router.get('/dialogue/{prompt}')
def get_dialogue(prompt:str):
    return lit_service.get_dialogue(prompt)



@router.get('/nonfiction/{prompt}')
def get_nonfiction(prompt:str):
    return lit_service.get_nonfiction(prompt)

@router.get('/novel/{prompt}')
def get_novel(prompt:str):
    return lit_service.get_novel(prompt)

@router.get('/script/{prompt}')
def get_script(prompt:str):
    return lit_service.get_script(prompt)


