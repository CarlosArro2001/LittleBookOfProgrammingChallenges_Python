from random import randint
suits = ["Clubs","Diamonds","Hearts","Spades"]
num = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
new_Cards=[]
newCard = " "
randNum = 0
randSuit = 0
counter = 0 
if(randNum == "Ace" or randNum == "Jack" or randNum == "Queen" or randNum == "King"):
    newCard ="{0} of {1}".format(randNum,randSuit)
else:
    newCard ="{0} {1}".format(randSuit,randNum)
new_Cards.append(newCard)

while(len(new_Cards)-1 != 52):
    randSuit = suits[randint(0,3)]
    randNum = num[randint(0 , 12)]
    newCard = ""
    if(randNum == "Ace" or randNum == "Jack" or randNum == "Queen" or randNum == "King"):
        newCard ="{0} of {1}".format(randNum,randSuit)
    else:
        newCard ="{0} {1}".format(randSuit,randNum)
    print(newCard)
    match = False
    for i in new_Cards:
        if( i == newCard):
            print("Duplicate")
            match = True
            break
    if(match == False):
        new_Cards.append(newCard)

