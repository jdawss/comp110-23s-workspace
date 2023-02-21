"""Creating a wordle that must be done in one shot."""

__author__ = "730474369"

# Defining the secret word variable"
the_word: str = "python"

# Defining the index for the word"
word_idx: int = 0

# Defining the emoji storage
emoji_store: str = ""

# Defining the variables of the colored boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Defining the variable for the answer input by user
six_let: str = input(f"What is your {len(the_word)}-letter guess? ")

# Creating the loop for length of word and giving answers based on input by user
while len(six_let) != len(the_word):
    six_let = (input(f"That was not {len(the_word)} letters! Try again:"))
if six_let == the_word:
    print(" Woo! You got it! ")   
else:
    print(" Not quite. Play again soon! ") 
    
# Creating loop and boolean sequences for the output of Green, white, and yellow boxes based on correctness at each index
while word_idx < len(the_word):
    if six_let[word_idx] == the_word[word_idx]:
        emoji_store += GREEN_BOX
    else:
        in_word: bool = False
        other: int = 0
        while in_word is False and other < len(the_word):
            if the_word[other] == six_let[word_idx]:
                in_word = True
            other = other + 1
        if in_word is True:
            emoji_store = emoji_store + YELLOW_BOX
        else:
            emoji_store += WHITE_BOX
    word_idx += 1

# Printing the emojis
print(emoji_store)