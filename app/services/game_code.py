import random
import string


def generate_game_code():
    # do we need to check if the game code is already in use?
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
