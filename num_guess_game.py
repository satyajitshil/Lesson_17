import random

random.seed(5)
answer = random.randint(10,20)
print("Welcome to the games. You must pick the correct number or face the consequences...")
print("Or just win the game!")
playing = True
while playing:
    b = int(input("Pick a number..."))
    if b == answer:
        print("You beat the game!!!")
        print("Plz play again.")
        break
    else:
        print("Face the consequences... by continuing to PLAY!!!")
        
        