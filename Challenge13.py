from random import randint 

i = randint(20,30)
while( i != 0):
    print("How many do you want to remove : ")
    player = int(input())
    i = i-player
    if(i == 0 or i < 0):
        print("PLAYER WINS ")
        break
    else:
        print("{0} left".format(i))
    computer = randint(1,3)
    i = i - computer
    if(i == 0 or i < 0):
        print("COMPUTER WINS")
        break
    else:
        print("{0} left".format(i))    