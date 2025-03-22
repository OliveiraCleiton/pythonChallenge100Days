# day 04, prject: Rock, Paper, Scissors
import random

game_options = ["Rock", "Paper", "Scissors"]
player_choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 fo Scissors."))
computer_choice = random.randint(0,2)

if player_choice  == computer_choice:
    print(f"draw the computer_choice is {game_options[computer_choice]}")
elif player_choice == 0 and computer_choice == 2:
    print(f"The computer choose is Scisoors, you")
elif player_choice == 1 and computer_choice == 0:
    print("You win, the computer chosse is rock")
elif player_choice == 2 and computer_choice == 1:
    print("You win, the computer chosse is Scissors")
else:
    print(f"The computer choose {game_options[computer_choice]}, you lose")

