import random

targetNumber = random.randint(0, 100)

while True:
    usersChoice = int(input("Enter a number between 0 and 100 : "))

    if(usersChoice == targetNumber):
        print("Congratulations! You guessed the number correct!\n")
        break
    elif(usersChoice > targetNumber):
        print("You guessed too high. Try a small one...\n")
    elif(usersChoice < targetNumber):
        print("You guessed too low. Try a bigone...\n")