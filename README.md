# Lost Island Adventure

A beginner-friendly, deterministic Python CLI adventure game.

## Setup

Requires Python 3.9+ and no third-party dependencies.

```bash
python3 main.py
```

## Run tests

```bash
python -m unittest 
```

## Map and rules

Intended adventure progression: **Beach → Jungle → Cave → Old Bridge → Lighthouse**. The main menu permits revisiting areas in any order; the Cave uses its own submenu. The map is a story guide, not strict adjacency-based movement.

- Start at the Beach with **5 energy** and an empty inventory.
- Beach: collect **rope** once, no energy cost.
- Jungle: collect **lantern** once; each visit costs 1 energy.
- Cave: exploring deeper costs 1 energy; returning to Beach costs none.
- Old Bridge: requires rope; the first successful crossing costs 1 energy. Once crossed, revisiting the bridge is free.
- Lighthouse: requires lantern, successful bridge crossing, and energy above zero. Activating it wins.
- A legal action that spends the final energy point causes an immediate loss; energy never drops below zero.
- Invalid inputs/actions do not change state or spend energy.
- Quit, win, and lose end the round; the player may replay with reset state.

## Code structure

- `main.py`: command-line input, presentation, and replay.
- `game.py`: deterministic rules; `new_game`, `available_actions`, `apply_action`, `is_win`.
- `tests_game_test.py`: automated unit tests without interactive typing.

## Limitations

- Text-only gameplay; no save/load or random events.
- Main menu allows choosing areas in any order, rather than enforcing adjacency.
- Lighthouse activation is permitted from the main menu after prerequisites are met.

## Git basics

```bash
git clone
git status
git add .
git commit -m "Build Lost Island CLI adventure"
git switch -c feature/improve-map
```

Use `git clone <repository-url>` to copy an existing repository. Configure Git name/email if prompted.