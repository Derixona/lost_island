# PROGRAMME DESIGN AND DECISION # 

### PROJECT DESIGN/FUNCTIONS ###

- Each rules/duties of the game was implemented as a function i.e one function one responsiblility example of the functions you will likely come across in this project are:
1. *** def new_game() *** which returns the game details including players name if provided by the player if not the default (name = "Explorer") is set as the players name.

2. *** def available_actions() *** responsible for returning all approve menu required by the game. e.t.c

### DECISIONS ###

- Python List[] is used as the type() for the inventory why because we know the user is expected to collected an iteam but we don't know the quantity so in this case we use list[] to be able to store multiple values of different datatypes.

## AI LEARNING AND RECOMMENDATIONS ###

#### WHAT I DID ####

````python
if inventory == []:
    print("No items in inventory")
````
#### AI RECOMMENDATION ####

````python
if not inventory:
    print("No items in inventory")
````
- AI was also use ti check for missed flaws and edge cases that i may have missed.