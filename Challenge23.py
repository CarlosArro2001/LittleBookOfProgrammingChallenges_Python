map = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
found = False
while(found != True):
    print("Enter coordinate 1 : ")
    n1 = int(input())
    print("Enter coordinate 2 : ")
    n2 = int(input())
    if(map[n1][n2] != map[4][5]):
        print("No Treasure , search somewhere else")
    else:
        print("TREASURE FOUND")
        found = True