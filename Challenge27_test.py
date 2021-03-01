print("Player 1 please enter a word")
player1 = input()
word_List = list(map(str,player1))
for i , x in enumerate(word_List):
    print("{0} {1}".format(i,x))  