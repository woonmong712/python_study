print('''
              ________
             / ______ \
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      ^~^  ,
             ||______||     ('Y') )
            /__________\    /   \/
    ________|__________|__ (\|||/) _________
   hjw     /____________\
   `97     |____________|
''')
print("Welcome to WOONMONG Company.")
print("Your mission is to find the door and go to work without overtime.")

# Write your code below this line 👇
choice1 = input(
    "You're at a crossroad, where do you want to go? Type 'left' or'right'.").lower()
if choice1 == "right":
    # Continue the game
    choice2 = input(
        "Great job. You got on the elevator. What floor would you like to go down? (1 ~ 10)")
    if choice2 == "3":
        # continue
        choice3 = input(
            "There is a door leading down to the first floor stairs. Each door is painted red, yellow and blue. Which door would you choose? (red, yellow, blue)")
        if choice3 == "yellow":
            print("Congratulations. You left work on time. Go home right now! ^_^v")
        else:
            print(
                "The phone rings. They say there is overtime. You go back to your seat to work overtime. T_T")
    else:
        print("Suddenly the elevator broke down and stopped. You are unable to leave work on time.")
else:
    print("You met your boss. Return to your seat.")
