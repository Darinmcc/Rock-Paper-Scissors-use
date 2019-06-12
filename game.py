
import random

print("--------------------")
print("Welcome to My Rock, Paper, Scissors Game!")
print("--------------------")

print("Let's begin:")

user_choice = input("Please choose: 'rock', 'paper', 'scissors':")

print("--------------------")
print("USER CHOICE:",user_choice)


options = ["rock", "paper", "scissors"]

if user_choice in options:
    pass
else:
    print("INVALID SELECTION. PLEASE TRY AGAIN.")
    exit()

print("Generating......")

computer_choice = random.choice(options)

print("COMPUTER CHOICE:", computer_choice)

print("Rock, Paper, Scissors, Shoot!")


