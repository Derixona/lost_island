""" CLI interface for Lost Island Adventure."""

import time

from game import new_game, available_actions, apply_action, is_win


MAIN_MENU = {
    "1": ("Explore the Beach", "beach"),
    "2": ("Enter the Jungle", "jungle"),
    "3": ("Enter the Cave", "cave"),
    "4": ("Cross the Old Bridge", "bridge"),
    "5": ("Enter the Lighthouse", "lighthouse"),
    "6": ("Check your inventory", "inventory"),
    "7": ("Quit", "quit"),
}
CAVE_MENU = {
    "1": ("Explore deeper", "explore_deeper"),
    "2": ("Return to safety", "return_to_safety"),
    "7": ("Quit", "quit"),
}


def welcome_player():
    for word in "Welcome To the Lost Island...".split():
        print(word, end=" ", flush=True)
        time.sleep(0.3)
    print("\n")
    name = input("What is your name? ").strip()
    return name or "Explorer"


def choose_action(player):
    """Read and validate one menu selection without changing the game state."""
    menu = CAVE_MENU if player["location"] == "Cave" else MAIN_MENU
    print("\nWhat would you like to do?")
    for number, (label, _) in menu.items():
        print(f"[{number}] {label}")
    choice = input("Enter your choice: ").strip()
    if choice not in menu:
        print("Invalid choice! Select one of the listed numbers.")
        return None
    action = menu[choice][1]
    return action if action in available_actions(player) else None


def ask_replay():
    while True:
        answer = input("\nPlay again? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please enter yes or no.")


def main():
    name = welcome_player()
    while True:
        player = new_game(name)
        print(f"\nWelcome, {name}! Location: Beach | Energy: 5")
        print("Find a rope and lantern, cross the bridge, and light the Lighthouse.")

        while not player["game_over"]:
            action = choose_action(player)
            if action is None:
                continue
            print(apply_action(player, action))
            if not player["game_over"]:
                print(f"Current location: {player['location']} | Energy: {player['energy']}")

        if player["won"]:
            print("Congratulations! You survived the Lost Island!")
        elif not player["quit"]:
            print("GAME OVER! You did not survive the Lost Island.")

        if not ask_replay():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()