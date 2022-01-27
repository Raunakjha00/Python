# a=int(input("Enter number of rows you wanna print the star pattern"))
# b=bool(int(input("Enter 1 for normal pattern of star pattern \n Enter 0 for inverted star pattern ")))

# if b==True:
#     for i in range(1,a+1,2):
#         print(i*"*")
#         if i==a:
#             print("You result is as above and our program is leaving now")
# elif b==False:
#     while a!=0:
#         print(a*"*")
#         a=a-1
#         if a==0:
#             print("You result is as above and our program is leaving now")













# from itsdangerous import NoneAlgorithm


# a=int(input(('Enter number of rows of stars you want:-')))
# b=bool(int(input("Enter 1 for normal patern \t and 0 for reversed pattern")))
# if b==True:
#     for i in range(1,a+1):
#         print(i*'*')
# elif b==False:
#     for i in range(a,0,-1):
#         print(i*"*")




















import random
q=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50
a=random.choice(q)
# number_guessing game 
print("Number of guess is limited upto 9")
number_of_guess=1
while number_of_guess<=9:
    b=int(input("Enter your guess between 0 to 50 :-"))
    if number_of_guess==1 and b==a:
        print("Unbelivable!You won on your first try")
        break
    elif b==a:
        print(f'You gave the correct answer in { 9-number_of_guess }  times')
        print("Congrats! You won")
        break
    elif b<a:
        print(f"You answer is less than actual oneand you have {9-number_of_guess} chances")
    elif b>a:
        print(f"You answer is more than actual oneand you have {9-number_of_guess} chances")
    elif number_of_guess>9:
        print("Sorry but number of chances have finished means You lose! Better luck next time")
    
    number_of_guess=number_of_guess+1
    pass










