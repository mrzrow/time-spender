from fastapi import APIRouter

from backend.core.config import settings
from backend.api.user.views import router as user_router
from backend.api.event.views import router as event_router

router = APIRouter(prefix=settings.api_prefix)
router.include_router(router=user_router)
router.include_router(router=event_router)
