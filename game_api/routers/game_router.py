from fastapi import APIRouter

from . import auth
from . import users
from . import games

router = APIRouter()

router.include_router(auth.router)
router.include_router(users.router)
router.include_router(games.router)
