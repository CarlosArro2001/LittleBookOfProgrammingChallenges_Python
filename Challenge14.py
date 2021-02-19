from random import randint

i = 0 
n = []
#inserting random values between 1 - 13
while(i < 10):
    n.append(randint(0,13))
    i = i + 1
print(n)
print("Starting number : {0}".format(n[0]))
i = 0
c = 0 
while(i < len(n)-1):
    print("Higher(H) or Lower(L) ?")
    p = input()
    if((p == "H" and n[i+1] > n[i]) or (p=="L" and n[i+1] < n[i])):
        print("CORRECT \n Next number : {0}".format(n[i+1]))
        c = c+1
        i = i+1
    else:
        print("Wrong")