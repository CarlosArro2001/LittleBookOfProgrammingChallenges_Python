def Challenge4():
    print("Enter speed :")
    speed = int(input())
    print("Enter time :")
    time = int(input())
    dist = speed*time
    print(dist)

def Challenge4Extension():
    print("Enter Distance in metres : ")
    dist = int(input())
    print("Enter Time in seconds : ")
    time = float(input())
    speed = dist/time
    print("Speed needed to travel at {0}m  in {1} seconds is : {2} m/s".format(dist,time,speed))

Challenge4()
Challenge4Extension()