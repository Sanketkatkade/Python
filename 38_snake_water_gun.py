import random

total = 0
scoreP = 0
scoreC = 0
draw = 0

while True:
    mylist = ["S", "W", "G"]
    res = random.choice(mylist)

    print("Enter your choise form : S, W ,G - Enter q to exit")
    a = input("[#] Your Choice : ")
    if a == "q":
        print(f"Your score is {scoreP}", f"Computers Score is {scoreC}")
        print("\nYou win the game") if (scoreP >= scoreC) else print(
            "\nComputer won the game"
        )
        print("\nThanks for playing")
        break
    if a not in mylist:
        print("Invalid input! try again...")
        continue
    total += 1
    print("[$] Computers Choice : ", res)

    if res == a:
        print("Do one more time\n")
        draw += 1
    elif res == "S" and a == "W":
        print("Computer wins\n")
        scoreC += 1
    elif res == "S" and a == "G":
        print("You wins\n")
        scoreP += 1
    elif res == "W" and a == "S":
        print("You wins\n")
        scoreP += 1
    elif res == "W" and a == "G":
        print("Computer wins\n")
        scoreC += 1
    elif res == "G" and a == "W":
        print("You wins\n")
        scoreP += 1
    elif res == "G" and a == "S":
        print("Computer wins\n")
        scoreC += 1
