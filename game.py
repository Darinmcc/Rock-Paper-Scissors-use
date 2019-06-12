
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

#determine the winner
#rock beats scissors
#paper beats rock
#scissors beat paper

if user_choice == computer_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "paper":
    print("Sorry, better luck next time!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("Congratulaions, you WON!")

elif user_choice == "paper" and computer_choice == "scissors":
    print("Sorry, better luck next time!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Congratulaions, you WON!")

elif user_choice == "scissors" and computer_choice == "rock":
    print("Sorry, better luck next time!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Congratulaions, you WON!")

print("Play again?")
exit()

#cd C:/Users/dmccollum/Documents/GitHub/Rock-Paper-Scissors-use


