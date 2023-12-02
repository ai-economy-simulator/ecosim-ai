from fastapi import APIRouter
from app.interfaces.game_code import NewGameCodeGETRequest, NewGameCodeGETResponse
from app.services.game_code import generate_game_code

router = APIRouter(prefix="/game-code", tags=["gameCode"])


@router.get("/new")
def new_game_code():
    response = NewGameCodeGETResponse(game_code=generate_game_code())
    print(response.model_dump(by_alias=True))
    return response.model_dump(by_alias=True)
