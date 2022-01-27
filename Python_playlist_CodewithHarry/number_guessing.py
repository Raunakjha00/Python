# n=22

# a=int(input("Enter a number"))
# guesses=1
# while guesses<=4:
#     number_guess=int(input("Enter a number you guessed \n"))
#     if number_guess>22:
#         print("Sorry!but number you entered is greater than actual one")
#     elif number_guess<22:
#         print("Sorry!but number you entered is lesser  than actual one")
#     else:
#         print(f"You won in {guesses} times")
#     if guesses>14:
#         break





n=44
number_of_guesses=1
print("Number of guesses is only limited to 9 times")
while number_of_guesses<=9:
    guess_number=int(input("Enter a number \n"))
    
    if guess_number>44:
        print(f'Your guess is more than actual one and you have {9-number_of_guesses} Chances')
    elif guess_number<36:
        print(f'Your guess is less than actual one and you have {9-number_of_guesses} Chances')
    else:
        print(f"You won the game in {number_of_guesses} Guesses")
        break

    number_of_guesses=number_of_guesses+1
    if(number_of_guesses>9):
        print("The end! You lose")
        break


a=int(input("Enter a number \n"))
s=1
while s<101:
    print(f' {a} x {s} = {a*s}')
    s=s+1
