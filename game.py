def new_game(name="Explorer"):
    """Return an independent starting state for one adventure."""
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "bridge_crossed": False,
        "game_over": False,
        "won": False,
        "quit": False,
    }


def available_actions(player):
    """Return the actions currently available in the menu."""
    if player["game_over"]:
        return []
    if player["location"] == "Cave":
        return ["explore_deeper", "return_to_safety", "quit"]
    return ["beach", "jungle", "cave", "bridge", "lighthouse", "inventory", "quit"]


def is_win(player):
    """Whether the player successfully  reach the Lighthouse."""
    return player["won"]
