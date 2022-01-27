#use random
#use random.choice
import random
a='s','w','g'
player_win=0
computer_win=0
num_of_chances=1
while num_of_chances<=10:
    c=random.choice(a)
    print("computer choosed now it is your turn")
    b=input("Enter 's' to choose snake  'g' for gun and 'w' for water \n")
    if b==c:
        print("Tie")
    elif b=='s' and c=='w':
        print(f"You won this time because computer had choosed {c}")
        player_win+=1
    elif b=='s' and c=='g':
        print(f"Computer won this time because computer had choosed {c}")
        computer_win+=1
    elif b=='w' and c=='g':
        print(f"You won this time because computer had choosed {c}")
        player_win+=1
    elif b=='w' and c=='s':
        print(f"Computer won this time because computer had choosed {c}")
        computer_win+=1
    elif b=='g' and c=='s':
        print(f"You won this time because computer had choosed {c}")
        player_win+=1
    elif b=='g' and c=='w':
        print(f"Computer won this time because computer had choosed {c}")
        computer_win+=1
    else :
        print(f"Sorry but we can't get it")
    num_of_chances=num_of_chances+1

if player_win>computer_win:
    print(f"You won because you won total{player_win} rounds")
elif computer_win>player_win:
    print(f" Computer won because computer won total {computer_win} rounds")
else:
    print("Tie")

    