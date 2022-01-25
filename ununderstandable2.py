# from cgi import print_directory


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













a=int(input(('Enter number of rows of stars you want')))
b=bool(int(input("Enter 1 for normal patern \t and 0 for reversed pattern")))
if b==True:
    for i in range(1,a+1):
        print(i*'*')
elif b==False:
    for i in range(a+1,1,-1):
        print(i*"*")





















