from pydantic import BaseModel


class NewGameCodeGETRequest(BaseModel):
    pass


class NewGameCodeGETResponse(BaseModel):
    game_code: str
