'''
Create a program with the following record structure
    Structure Results
        HomeTeam as string
        HomeTeamScore as integer
        AwayTeam as string
        AwayTeamScore as integer
    End Structure
Make an array of 20 Results

Create a program with a menu whose options are
    1. Add a result
    2. Search for all results for a team

Write the code to carry out these two things.

If option 1 is selected
    1.collect the result and add it to the end of the results array

If option 2 is selected
    1.Collect team name
    2.display all the results that in includes that team in either the
home or away team

Author : Carlos Raniel Ariate Arro 
'''

import sys 
global result 
result = [[["Blue",2],["Red",3]],[["Purple",3],["Blue",4]],[["Red",1],["Purple",0]],[["Orange",5],["Red",1]]]

#Menu to choose "1" for adding result or "2" for Searching results for a team
def menu():
    choice = 0
    while(choice != 3):
        no_Results = len(result)
        print("{0} results.".format(no_Results))
        print("Enter 1 to add a result.")
        print("Enter 2 to Search for all results for a team")
        print("Enter 3 to Exit  ")
        choice = int(input())
        if(choice == 1):
            setResult()
        if(choice == 2):
            getResult()
        #closing the program if 3 is selected 
        if(choice == 3):
            sys.exit()
#method for adding new results in
def setResult():
    print("Enter home team")
    home = input()
    print("Enter home point")
    h_Point = int(input())
    print("Enter away team")
    away = input()
    print("Enter away point")
    a_Point = int(input())
    new_Result = [[home,h_Point],[away,a_Point]]
    result.append(new_Result)
    print(result)

#method for getting results for a specific team 
def getResult():
    print("Enter team to search for :")
    team = input()
    result_Query = []
    for i in result:
        if(i[0][0] == team or i[1][0] == team ):
            result_Query.append(i)
    if(len(result_Query) == 0):
        print("No results found")
    else:
        for i in result_Query:
            print("{0} | {1}".format(i[0],i[1]))
        result_Query.clear()

menu()