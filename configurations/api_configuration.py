from fastapi import FastAPI, APIRouter
app = FastAPI()
router = APIRouter()

app.include_router(router, prefix = "api/v1/")