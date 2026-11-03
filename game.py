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


def apply_action(player, action):
    """Apply a valid action and return a message; invalid actions change nothing."""
    if action not in available_actions(player):
        return "Invalid action! Please choose an available option."

    if action == "quit":
        player["quit"] = True
        player["game_over"] = True
        return "Thanks for playing!"

    if action == "inventory":
        items = ", ".join(player["inventory"]) or "empty"
        return f"Inventory: {items} | Location: {player['location']} | Energy: {player['energy']}"

    if action == "beach":
        player["location"] = "Beach"
        if "rope" not in player["inventory"]:
            player["inventory"].append("rope")
            return "You explored the Beach and found a rope!"
        return "You explored the Beach. You already collected the rope."

    if action == "jungle":
        player["location"] = "Jungle"
        player["energy"] = max(0, player["energy"] - 1)
        if player["energy"] == 0:
            player["game_over"] = True
            return "You entered the Jungle, exhausted your energy, and lost!"
        if "lantern" not in player["inventory"]:
            player["inventory"].append("lantern")
            return f"You entered the Jungle and found a lantern! Energy: {player['energy']}"
        return f"You entered the Jungle. You already have the lantern. Energy: {player['energy']}"

    if action == "cave":
        player["location"] = "Cave"
        return "You entered a dark Cave. Explore deeper or return to safety?"

    if action == "explore_deeper":
        player["energy"] = max(0, player["energy"] - 1)
        if player["energy"] == 0:
            player["game_over"] = True
            return "You explored deeper, exhausted your energy, and lost!"
        return f"You explored deeper into the Cave. Energy: {player['energy']}"

    if action == "return_to_safety":
        player["location"] = "Beach"
        return "You safely returned to the Beach. No energy lost."

    if action == "bridge":
        if "rope" not in player["inventory"]:
            return "You need a rope to cross the Old Bridge!"
        if player["bridge_crossed"]:
            player["location"] = "Old Bridge"
            return "You have already crossed the Old Bridge."
        player["energy"] = max(0, player["energy"] - 1)
        if player["energy"] == 0:
            player["game_over"] = True
            return "You ran out of energy while crossing the bridge. Game Over!"
        player["bridge_crossed"] = True
        player["location"] = "Old Bridge"
        return f"You successfully crossed the Old Bridge! Energy: {player['energy']}"

    if action == "lighthouse":
        missing = []
        if "lantern" not in player["inventory"]:
            missing.append("lantern")
        if not player["bridge_crossed"]:
            missing.append("successful bridge crossing")
        if missing:
            return "Requirements not met: you need " + " and ".join(missing) + "."
        player["location"] = "Lighthouse"
        player["won"] = True
        player["game_over"] = True
        return "🏆 You activated the Lighthouse! A rescue ship spotted your signal. YOU WIN!"

    return "Invalid action!"