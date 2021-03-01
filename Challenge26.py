num = 2019
code = list(map(int,str(num)))

counter = 0
while(counter != 12):
    print("Enter a 4 digit code : ")
    user_Enter = int(input())
    guess = list(map(int,str(user_Enter)))    
    if(user_Enter == num):
        print("MATCH")
        break
    else:
        for i in guess:
            print(i)
            for x in code:
                if( i == x):
                    print("Match : {0}".format(i))
        
    counter += 1 
