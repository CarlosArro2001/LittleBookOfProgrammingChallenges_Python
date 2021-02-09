def challenge3():
    print("Input width :")
    w = int(input())
    print("Input height:")
    h = int(input())
    area = h * w 
    print("Area : {0}".format(area))
    
def challenge3Extension():
    print("Input width :")
    w = int(input())
    print("Input height:")
    h = int(input())
    print("Input length:")
    l = int(input())
    vol = l * h * w
    print("Volume : {0}".format(vol))

challenge3()
challenge3Extension()