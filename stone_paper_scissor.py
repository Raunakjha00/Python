import random
print("This game will be of 10 rounds")
rounds=1
computer=0
player=0
c=("r","p", "s") 
while rounds<=10:
    d=random.choice(c)
    print("Computer had guesseed now you should guess")
    print(d)
    a=input("Enter 'r' for rock 'p' for paper and 's' for scissors:-  ")
    if a==d:
        print("Tie ")
    elif a=='r' and d=='s':
        print(f'You won this round because computer had selected scisoors')
        player+=1
    elif a=='r' and d=='p':
        print(f"You lose this round because computer had selected paper ")
        computer+=1
    elif a=='p' and d=='r':
        print(f'You won this round because computer had selected rock ')
        player+=1
    elif a=='p' and d=='s':
        print(f"You lose this round because  computer had selected scissors")
        computer+=1
    elif a=='s' and d=='p':
        print(f"You won this round because  computer had selected paper")
        player+=1
    elif a=='s' and d=='r':
        print(f"You lose this round because  computer had selected rock")
        computer+=1
    else:
        print(f"Sorry we can't get it{d} ")
        
    rounds=rounds+1
    
if player>computer:
    print(f"You won because you won {player} rounds")
elif player<computer:
    print(f"computer won because computer won {computer} rounds")
else:
    print(f"Tie because both of you have won equal rounds and number of rounds is {rounds} ")

    
