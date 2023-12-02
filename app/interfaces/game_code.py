from .main import AliasedBaseModel


class NewGameCodeGETRequest(AliasedBaseModel):
    pass


class NewGameCodeGETResponse(AliasedBaseModel):
    game_code: str
