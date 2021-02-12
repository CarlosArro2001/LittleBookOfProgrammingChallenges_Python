from random import randint
#suit
suit = ["Clubs","Diamonds","Hearts","Spades"]
#numbers 
num = ["Ace","1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
print("How many cards do you want? ")
i = int(input())
counter = 0
while(counter < i ):
    rand1 = randint(0,len(suit)-1)
    rand2 = randint(0,len(num)-1)
    if(num[rand2] == "Ace" or num[rand2] == "Jack" or num[rand2] == "Queen" or num[rand2] == "King"):
        print("{0} of {1}".format(num[rand2],suit[rand1]))
    else:
        print("{0} , {1}".format(num[rand2],suit[rand1]))
    counter += 1 
