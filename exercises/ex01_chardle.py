"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730474369"

fivchr: str = input("Enter a 5-character word: ")
if len(fivchr) != 5:
    print(" Error: Word must contain 5 characters ")
    exit()
sinchr: str = input("Enter a single character: ")
if len(sinchr) != 1:
    print(" Error: Character must be a single character. ")
    exit()
print("Searching for " + sinchr + " in " + fivchr)

chrnum = 0
    
if sinchr == fivchr[0]:
    print(sinchr + " found at index 0 ")
    chrnum +=1
if sinchr == fivchr[1]:
    print(sinchr + " found at index 1 ")
    chrnum +=1
if sinchr == fivchr[2]:
    print(sinchr + " found at index 2 ")
    chrnum +=1
if sinchr == fivchr[3]:
    print(sinchr + " found at index 3 ")
    chrnum +=1
if sinchr == fivchr[4]:
    print(sinchr + " found at index 4 ")
    chrnum +=1
    
if chrnum == 0:
    print("No instances of " + sinchr + " found in " + fivchr)
if chrnum == 1:
    print(str(chrnum) + " instance of " + sinchr + " found in " + fivchr)
else:
    print(str(chrnum) + " instances of " + sinchr + " found in " + fivchr)
 