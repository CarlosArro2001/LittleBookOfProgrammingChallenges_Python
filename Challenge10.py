from random import randint

rps = ["R","P","S"]
computer = rps[randint(0,len(rps)-1)]
print("Enter R for rock . Enter P for paper . Enter S for Scissors")
player = input()
if((computer == "R" and player=="S")or(computer == "P" and player=="R")or(computer == "S" and player=="P")):
    print(computer)
    print("Computer Wins")
elif((computer == "S" and player=="R")or(computer == "R" and player=="P")or(computer == "P" and player=="S")):
    print(computer)
    print("Human Wins")
