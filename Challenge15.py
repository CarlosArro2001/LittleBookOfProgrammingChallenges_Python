s = "Hello my name is Carlos"
i = 0 
c = 0
#checking if the string does not have a space in the end 
if(len(s)!= ' '):
    c += 1
while(i < len(s)):
    if(s[i] == ' '):
        c += 1
    i +=1 
print("{0} words found.".format(c))