a=int(input("Enter number of rows you want"))
b=bool(int(input("Enter True or false")))
z=1
if b==True:
    while z<=a:
        print(z*"*")
        z=z+1
        # break
elif b==False:
    while a!=0:
        print(a*"*")
        a=a-1
        # if b==True:
#     for i in range(1,a+1):

#         for a in range(1,i+1):

#             print("*", end =" ")
#     print()
# elif b== False:
#     for i in range(a,0,-1):

        

#         print("*", end=" ")
#     print()
a = int(input("Enter the number of rows you want in the star pattern : "))

b = bool(int(input("Enter 1 if you want straight star pattern \nEnter 0 if you want inverted star pattern \n")))

if b == True :

    for i in range(a) :

        print((i+1)*"*")

elif b == False :

    while a != 0 :

        print(a*"*")

        a = a-1