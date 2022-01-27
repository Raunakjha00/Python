a=22  
number_of_guess=1
print(f"You have total 9 chances")
while number_of_guess<10:
    
    d=int(input("Enter  a  number between 0 to 50 \n"))  
    if d==a:
        print(f'You said the right answer in {number_of_guess} times') 
        print("The End! Victory")
        break
    elif d>a:
        print(f"Your answer is wrong and you have{9 -number_of_guess} guesses")
    elif d<a:
        print(f'Your answer is wrong and you have {9 -number_of_guess} guesses ')
    number_of_guess=number_of_guess+1    
    pass