'''
Write a procedure(sub) drawstars that will draw a 
sequence of spaces followed by a sequence of stars. 
It should accept two parameters—the number
of spaces and the number of stars.

Drawstars(3,5) would produce
_ _ _ * * * * * ( _ indicates a space!)
'''

def Drawstars(space,stars):
    #drawing the spaces and stars
    s = " "
    st = "*"
    for i in range(space):
        print(s,end='')
    for x in range (stars):
        print(st,end='')

def DrawPyramid(base):
    i = 0 
    while(i < base):

        for x in range(i):
            print(" ",end='')
            print("*",end='')
        print("")
        i += 1
DrawPyramid(5)

'''    
Drawstars(3,3)
print()
Drawstars(3,3)
print()
Drawstars(4,1)
print()
Drawstars(3,3)
print()
Drawstars(1,7)
print()
Drawstars(3,3)
print()
Drawstars(3,1) 
Drawstars(1,1)
print()
Drawstars(2,2)
Drawstars(1,2)
'''