"""Adventure game."""

__author__ = "730474369"

import sys
import random

# Initialize global variable points
points: int = 0

# Initialize global variable player
player: str = ""

# Define emoji constant
TREASURE_EMOJI = "💰"

def greet() -> None:
    """Greeting the player."""
    global player
    print("Welcome to the treasure cove!")
    player = input("What is your name?\n")

def path1() -> None:
    """Defining the first path."""
    global points
    print(f"{player}, you have chosen Blackbeard's Bounty.")
    print(f"You find a treasure chest! {TREASURE_EMOJI}")
    points += 10
    print(f"You gained 10 pirate points. You now have {points} pirate points.")

def path2() -> None:
    """Defining the second path."""
    global points
    print(f"{player}, you have chosen the Smoky Mountain.")
    print("You encounter a dragon!")
    choice = input("What do you do? Run or fight?\n")
    if choice == "fight":
        print("You defeated the dragon and gained 5 pirate points!")
        points += 5
    else:
        print("You ran away from the dragon and lost 3 pirate points!")
        points -= 3
    print(f"You now have {points} pirate points.")

def path3() -> None:
    """Defining the third path."""
    global points
    print(f"{player}, you have chosen the Lost Souls' Lair.")
    print("You are in a maze!")
    direction = input("Do you want to go left or right?\n")
    choices = {"left": 7, "right": -5}
    if direction in choices:
        points += choices[direction]
        print(f"You now have {points} pirate points.")
    else:
        print("Invalid choice. Try again.")

def main() -> None:
    """Defining the main function."""
    greet()
    global points
    points = 0

    paths = [path1, path2, path3]

    while True:
        print("Choose your path:")
        print("1. Path 1")
        print("2. Path 2")
        print("3. Path 3")
        print("4. End the adventure")
        choice = input()

        choice = int(choice) if choice.isdigit() else None
        valid_choices = [1, 2, 3, 4]
        if choice in valid_choices:
            if choice == 4:
                print(f"Goodbye, {player}! You earned {points} pirate points.")
                break
            else:
                paths[choice - 1]()
                print(f"You now have {points} pirate points.")
        else:
            print("Invalid choice. Try again.")

    print(f"Thanks for playing, {player}!")

if __name__ == "__main__":
    main()