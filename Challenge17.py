'''
Write a function that will convert a UMS score into a grade. The
function will return ‘A’—> ‘U’.
The function will require a parameter to do its job: the mark
The formula for AS level is >=80% —>‘A’, >=70%—>‘B’, >=60%—>‘C’
etc.
'''
def getGrade(mark):
    #if mark is >=80 then A
    if (mark >= 80):
        return 'A'
    #if mark is >=70 and <=80 then B
    if (mark >= 70 and mark <=80):
        return 'B'
    #if mark is >= 60 and <=70 then C
    if (mark >= 60 and mark <=70):
        return 'C'
    #if mark is >=50 and <=60 then D
    if (mark >=50 and mark <=60):
        return 'D'
    #if mark is >=40 and <=50 then E
    if (mark >=40 and mark <=50):
        return 'E'
    #if mark is <= 40 then U
    if(mark < 40):
        return 'U'

def getGrade_Ext(max_mark,mark):
    prcnt = (mark/max_mark)*100
    #if mark is >=80 then A
    if (prcnt >= 80.0):
        return 'A'
    #if mark is >=70 and <=80 then B
    if (prcnt >= 70.0 and prcnt <=80.0):
        return 'B'
    #if mark is >= 60 and <=70 then C
    if (prcnt >= 60.0 and prcnt <=70.0):
        return 'C'
    #if mark is >=50 and <=60 then D
    if (prcnt >=50.0 and prcnt <=60.0):
        return 'D'
    #if mark is >=40 and <=50 then E
    if (prcnt >=40.0 and prcnt <=50.0):
        return 'E'
    #if mark is <= 40 then U
    if(prcnt < 40.0):
        return 'U'

print(getGrade_Ext(42,24))