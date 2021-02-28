#generating a fibonacci sequence
#0,1,1,2,3,5,8,13,...
#
fib = []
i = 0 
n1 = 0 
n2 = 1
n3 = 0
fib.append(n1)
fib.append(n2)
while(i < 50):
    n3 = n1+n2
    fib.append(n3)
    n1 = n2
    n2 = n3
    i = i+1
print("Which position in sequence? ")
choice = int(input())
print(fib[6])



