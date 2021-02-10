#time and math module used 
import time
import math
#alphabet to loop and compare with against user input
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#Telling user to hit enter key when ready 
print("Hit enter when Ready")
n= input()
#starting the loop and the timer 
i = 0 
s_Time = time.time()
print("TIMER STARTED")
while(i < len(alphabet)):
    #asking user to enter in alphabet(on a certain orrder)
    print("Enter {0}".format(alphabet[i]))
    n = input()
    #checking whether the input is correct regardless of uppercase or lower case 
    if(n == alphabet[i] or n == alphabet[i].upper()):
        print("Correct")
        i = i+1
#getting the endtime 
e_Time = time.time()
print("TIMER ENDED")
#outputting the time taken by doing e_Time - s_Time
print("Time : {0} seconds".format(math.ceil(e_Time-s_Time)))

