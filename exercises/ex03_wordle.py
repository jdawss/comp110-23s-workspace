"""Structured Wordle"""

__author__ = "730474369"

# Define the function contains_char which checks if a character is present in a word
def contains_char(wrd_srch: str, sing_chr: str) -> bool:
    """Returns True if chr is found at index of first string"""
    assert len(sing_chr) == 1
    indx = 0
    while indx < len(wrd_srch):
        if wrd_srch[indx] == sing_chr:
            return True
        indx += 1
    return False

# Intialize variable for different emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Defining the function emojified function to generate the emoji string for each users guess vs the secret word
def emojified(user_guess: str, secret_wrd: str) -> str:
    """Function returns string of emoji of different colors"""
    assert len(user_guess) == len(secret_wrd)

    # Initialize variables
    emoji_store = ""
    indx = 0

    # Loop through each character in the user's guess
    while indx < len(user_guess):
        # Check if the character in the user's guess is the same as the corresponding character in the secret word
        if user_guess[indx] == secret_wrd[indx]:
            emoji_store += GREEN_BOX
        else:
            in_word = contains_char(secret_wrd, user_guess[indx])
            if in_word:
                emoji_store += YELLOW_BOX
            else:
                emoji_store += WHITE_BOX
        indx += 1

    return emoji_store

# Define the function input_guess to get the users guess and make sure it has the expected number of chrs
def input_guess(expected_length: int) -> str:
    """Function for expected number of characters in a word"""
    while True:
        run = input(f"Enter a {expected_length} character word: ")
        if len(run) == expected_length:
            return run
        else:
            print(f"That wasn't {expected_length} chars! Try again: ")

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_wrd = "codes"
    turn_numb = 1
    max_turns = 6

    while turn_numb <= max_turns:
        print(f"=== Turn {turn_numb}/{max_turns} ===")
        user_guess = input_guess(len(secret_wrd))
        emoji_output = emojified(user_guess, secret_wrd)
        print(emoji_output)

        if user_guess == secret_wrd:
            print(f"You won in {turn_numb}/{max_turns} turns!")
            return
        turn_numb += 1

    print(f"X/{max_turns} - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()