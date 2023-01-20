"""if it's raining, tell me to pack umbrella"""

weather: str = input("what is the weather like? ")

if (weather == "rain"):
    print("Pack an umbrella! ")
    print("But splash in the puddles! ")
else:
    if weather == "snow":
        print("It's gonna be chilly lad! ")
    print("You don't need an umbrella! ")
print("Have a good day my boy! ")