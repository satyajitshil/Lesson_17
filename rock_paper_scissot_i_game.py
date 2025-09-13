import random

print("frontman: Welcome to the games Player. I am the frontman and you will be participating in the games. You win or get eliminated...")

options = ["Rock","Paper","Scissors"]
player_choice = input("Rock, Paper, or Scissor:")
cpu_choice = random.choice(options)

print("frontman: Let's see...")

if player_choice == cpu_choice:
    print("frontman: TIE!!! You have passed. On to the next game...")
elif player_choice == "Rock" and cpu_choice == "Scissors":
    print("frontman: You smashed the computer gaurd! On to the next game...")
elif player_choice == "Scissor" and cpu_choice == "Paper":
    print("frontman: You slashed apart the computer. WIll you make it through the next game...")
elif player_choice == "Paper" and cpu_choice == "Rock":
    print("frontman: You wrapped him up!!!!")
else:
    print("You have been eliminated by", cpu_choice ,"!!!... [update: player has been eliminated]")