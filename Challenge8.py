import datetime 
from datetime import date , timedelta
#asking user to enter birthday 
print("Enter day of birth in 'dd' format")
dd = int(input())
print("Enter month of birth in 'mm' format")
mm = int(input())
print("Enter year of birth in 'yyyy' format")
yyyy = int(input())
birthday = datetime.date(yyyy,mm,dd)
print("Birthday : {0} ".format(birthday))
#getting today date 
currDate = date.today()
print("Current Date : {0}".format(currDate))
#calculating the age using timedelta 
days_in_year = 365.2425
age = (currDate-birthday) // timedelta(days_in_year)
print("You are {0} years old ".format(age))
#checking if person is eligible to vote
if(age < 18 ):
    print("Unable to vote")
else:
    print("Able to vote for the next potato of the year")