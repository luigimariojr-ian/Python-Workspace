import random
playerchoice = input("Rock Paper or Scissors? ")
computeroptions = ["Rock", "Paper", "Scissors"]
computerchoice = random.choice(computeroptions)

print("Player: " + playerchoice + "!")
print("Computer: " + computerchoice + "!")

if playerchoice != "Rock" or playerchoice != "Paper" or playerchoice != "Scissors" or playerchoice != "rock" or playerchoice != "paper" or playerchoice != "scissors":
    print("Invalid Input :(")

if computerchoice == "Rock":
    if playerchoice == "Rock" or playerchoice == "rock":
        print("Tie!")
    if playerchoice == "Paper" or playerchoice == "paper":
        print("Player Wins!")
    if playerchoice == "Scissors" or playerchoice == "scissors":
        print("Computer Wins!")
if computerchoice == "Paper":
    if playerchoice == "Rock" or playerchoice == "rock":
        print("Computer Wins!")
    if playerchoice == "Paper" or playerchoice == "paper":
        print("Tie!")
    if playerchoice == "Scissors" or playerchoice == "scissors":
        print("Player Wins!")
if computerchoice == "Scissors":
    if playerchoice == "Rock" or playerchoice == "rock":
        print("Player Wins!")
    if playerchoice == "Paper" or playerchoice == "paper":
        print("Computer Wins!")
    if playerchoice == "Scissors" or playerchoice == "scissors":
        print("Tie!")