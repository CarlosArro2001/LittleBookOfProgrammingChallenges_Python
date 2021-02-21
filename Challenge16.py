from random import randint
rand_Num = randint(0,100)
print(rand_Num)
c = 0
p = 0
while(p!= rand_Num):
    print("Guess Here : ")
    p = int(input())
    if(p ==rand_Num):
        c+=1
        print("Got it")
    elif(p < rand_Num):
        c+=1
        print("Too low")
    elif(p > rand_Num):
        c+=1
        print("Too High")
print("You have {0} guesses".format(c))