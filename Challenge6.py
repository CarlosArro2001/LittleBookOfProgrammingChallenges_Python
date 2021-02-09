import time  
import math
#hit enter
n = input() 
#get start time
print("TIMER STARTED!")
s_Time = time.time()
#hit enter
n = input() 
#get end time
print("TIMER ENDED!")
e_Time = time.time()
#find difference between end & start ( end - start)
diff = e_Time - s_Time
#if diff = 0 output 'exactly on 10' if not 0 then output how close to 10 answer was 
if(math.ceil(diff) == 0.00):
    print("Exactly on 10")
else:
    print("You were at {0} seconds ".format(math.ceil(diff)))