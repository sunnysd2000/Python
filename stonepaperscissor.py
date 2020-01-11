import random
games=['stone','paper','scissor']
player_win=0
comp_win=0
new_player=""
new_player=input("Enter name of player:")
chances=random.randint(1,10)
computer=random.choice(games)
player=input("Choice from stone,paper,scissor:")
totalno=chances
while chances!=0:
    if computer==player:
        print("Computer played:",computer)
        print(new_player,"played:",player)
        print("Both wins")
        chances=chances-1
    elif(computer=="stone" and player=="scissor"):
        chances=chances-1
        comp_win+=1
        print("Computer played : Stone")
        print(new_player,"played: Scissor")
        print("***********Computer wins*********")
        
    elif(computer=="paper" and player=="stone"):
        chances=chances-1
        comp_win+=1
        print("Computer played : Paper")
        print(new_player,"played: Stone")
        print("*********Computer wins*******")
    elif(computer=="scissor" and player=="paper"):
        chances=chances-1
        comp_win+=1
        print("Computer played : Scissor ")
        print(new_player,"played: Paper")
        print("*********Computer wins************")
    else:
        chances-=1
        player_win+=1
        print("Player played:",player)
        print(new_player,"played :", computer)
        print("***********",new_player," wins************")
    computer=random.choice(games)
    player=input("Choice from stone,paper,scissor:")
if chances==0:
    print("----------RESULT-------------------")
    print("Total no of games played:",totalno)
    print("Computer wins",comp_win," times")
    print(new_player," wins",player_win,"times")
    
        
        