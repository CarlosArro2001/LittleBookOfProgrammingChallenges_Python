names = []
n = ""
i = 0
counter = 0
while(n != "exit"):
    print("Print name or exit")
    n = input()
    for i in names:
        if(n == i):
            print("{0} is a duplicate".format(n))
            counter += 1
    names.append(n)
print(names)

    
        