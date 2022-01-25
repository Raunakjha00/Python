# # #pattren printing
# # #Input=integer n
# boolean = True
# # *
# # **
# # ***
# # ****



print("How many rows do you want")
rows=int(input("Enter number of rows"))
a=bool(input("Enter true or False "))
if a==True:
    while True:
        print("*")
        
        pass
        
print("How Many Row You Want To Print")

one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:

    for i in range(1,one+1):

        for j in range(1,i+1):

            print("*",end=" ")

        print()
elif new ==False:
    for i in range(one,0,-1):

        for j in range(1,i+1):

            print("*", end="")
        print()
a=1
print(bool(a))
