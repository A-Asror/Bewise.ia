import fastapi

from backend.api.routes import question_router

router = fastapi.APIRouter()

router.include_router(router=question_router)
