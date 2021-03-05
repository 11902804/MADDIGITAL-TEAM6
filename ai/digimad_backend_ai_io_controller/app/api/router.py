from fastapi import APIRouter
from app.api.controllers.color_controller import router as colors
from app.api.controllers.emotion_controller import router as emotion
from app.api.controllers.emotion_lab_controller \
    import router as emotion_lab
from app.api.controllers.auth_controller import router as auth
from app.api.controllers.color_conversion_endpoints import router as conversion


router = APIRouter()
router.include_router(colors)
router.include_router(emotion)
router.include_router(emotion_lab)
router.include_router(auth)
router.include_router(conversion)