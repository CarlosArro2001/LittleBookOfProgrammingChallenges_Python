import datetime
from datetime import date
#Entering Date of birth
print("Enter day of birth : ")
day = int(input())
print("Enter month of birth : ")
month = int(input())
print("Enter year of birth : ")
year = int(input())
birthday = datetime.date(year,month,day)
print(birthday)
#Getting todays date 
print("Getting Todays date")
currDate = date.today()
print(currDate)
#Getting the diff between the two dates
diff = currDate - birthday
#Display Result 
print("You've been alive for:{0}".format(diff))