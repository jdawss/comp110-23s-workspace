"""Creating your own adventure game."""

from typing import List, Dict
import random

__author__: "730474369"

# Initialize global variable points
points: int = 0

# Initialize global variable player
player: str = ""

# Define emoji constant
TREASURE_EMOJI: str = "\U0001F4B0"

# Greet the player and ask for their name


def greet() -> None:
    """Greeting the player."""
    global player
    print("Welcome to the treasure cove!")
    player = input("What is your name?\n")


def path1() -> None:
    """Defining the first path."""
    global points, player
    print(f"{player}, you have chosen Blackbeard's Bounty.")
    print(f"You find a treasure chest! {TREASURE_EMOJI}")
    points += 10
    print(f"You gained 10 pirate points. You now have {points} pirate points.")


def path2() -> None:
    """Defining the second path."""
    global points, player
    print(f"{player}, you have chosen the Smoky Mountain.")
    
    # Randomly determine if the player encounters a dragon or not
    if random.random() < 0.5:
        print("You encounter a dragon!")
        choice: str = input("What do you do? Run or fight?\n")
        if choice == "fight":
            print("You defeated the dragon and gained 5 pirate points!")
            points += 5
        else:
            print("You ran away from the dragon and lost 3 pirate points!")
            points -= 3
    else:
        print("You explore the mountain and find a hidden cave with treasure!")
        points += 10
    
    print(f"You now have {points} pirate points.")


def path3() -> None:
    """Defining the third path."""
    global points, player
    print(f"{player}, you have chosen the Lost Souls' Lair.")
    print("You are in a maze!")
    direction: str = input("Do you want to go left or right?\n")
    choices: Dict[str, int] = {"left": 7, "right": -5}
    if direction in choices:
        points += choices[direction]
        print(f"You now have {points} pirate points.")
    else:
        print("Invalid choice. Try again.")


def main() -> None:
    """Defining main function."""
    global points
    greet()
    points = 0

    paths: List[None] = [path1, path2, path3]

    while True:
        print("Choose your path:")
        print("1. Path 1")
        print("2. Path 2")
        print("3. Path 3")
        print("5. End the adventure")
        choice: str = input()

        choice: int = int(choice) if choice.isdigit() else None
        valid_choices: List[int] = [1, 2, 3, 5]
        if choice in valid_choices:
            if choice == 5:
                print(f"Goodbye, {player}! You earned {points} pirate points.")
                return None
            else:
                selected_path = paths[choice - 1]
                selected_path()
                print(f"You now have {points} pirate points.")
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()