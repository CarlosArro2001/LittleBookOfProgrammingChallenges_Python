print("Player 1 please enter a word")
player1 = input()
word_List = list(map(str,player1))
covered_List = []
print(word_List)
i = 0
print("Word to Guess : ")
while(i<len(word_List)):
    print("*",end=" ")
    covered_List.append("*")
    i+=1
guess= 0
while(guess < 5):
    print("Enter a letter")
    player2 = input()
    match = False
    for i , x in enumerate(word_List):
        if(x == player2 or x.upper() == player2):
            covered_List[i] = player2
            print(covered_List)
            match = True
    if(match==False):
        guess+=1
        print("You have {0} guesses left".format(5 - guess))
    uncovered_List = ''.join(covered_List)
    if(uncovered_List == player1):
        print(uncovered_List)
        print("PLAYER 2 WINS")
        break
    
    