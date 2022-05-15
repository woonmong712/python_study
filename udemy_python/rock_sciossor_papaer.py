import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
play_dic = {0: rock, 1: paper, 2: scissors}
my_turn = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_turn = random.randrange(0, 2)
if my_turn >= 3 or my_turn < 0:
    print("You typed an invalid number, you lose!")
else:
    print(play_dic[my_turn])
    print("computer chose:")
    print(play_dic[computer_turn])

# if my_turn == computer_turn:
#   print("Draw")
# else:
#   if my_turn == 0:
#     if computer_turn == 1:
#       print("You lose")
#     elif computer_turn == 2:
#       print("You win")
#   if my_turn == 1:
#     if computer_turn == 1:
#       print("You lose")
#     elif computer_turn == 0:
#       print("You win")
#   if my_turn == 2:
#     if computer_turn == 0:
#       print("You lose")
#     elif computer_turn == 1:
#       print("You win")

    if my_turn == 0 and computer_turn == 2:
        print("You lose")
    elif my_turn == 2 and computer_turn == 0:
        print("You lose")
    elif computer_turn > my_turn:
        print("You Win!")
    elif my_turn > computer_turn:
        print("You win!")
    elif computer_turn == my_turn:
        print("It's a draw")
