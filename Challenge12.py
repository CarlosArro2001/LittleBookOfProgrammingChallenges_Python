# display all the factors of a number, entered by the user, that are bigger than 1.
print("Enter a factor bigger than 1 ")
n = int(input())
i = 2
isFactor = []
while(i < 12):
    print(i)
    if(n % i == 0):
        isFactor.append(i)
    if(i % 2 != 0):
        print("{0} is a prime number ".format(i))
    i = i+1
print(isFactor)