from fastapi import APIRouter
from app.interfaces.game_code import NewGameCodeGETRequest, NewGameCodeGETResponse
from app.services.game_code import generate_game_code

router = APIRouter(prefix="/gameCode", tags=["gameCode"])


@router.get("/new")
def new_game_code():
    response = NewGameCodeGETResponse(game_code=generate_game_code())
    return response
