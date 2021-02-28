from random import randint
arr = [[],[],[],[],[],[],[],[],[],[]]
for i in arr:
    x = 0 
    while(x < 10):
        r = randint(0,15)
        i.append(r)
        x += 1
print(arr)