a=input("Enter first number \n")
b=input("Enter second number \n")
c=input("Enter third number \n")

a=int(a)
b=int(b)
c=int(c)


if(type(a)== int):
    print("First number check ! Accomplished.You may continue")
else:
    print("Plz enter valid number in first input area")
if(type(b)== int):
    print("Second number check ! Accomplished. You may continue ")
else:
    print("Plz enter valid number in second input area. You may continue")
if(type(c)== int):
    print("Third number check ! Accomplished. You may continue")
else:
    print("Plz enter valid number in third input area")
z=( "Options are "+"product","sum","difference")
print(z)

userinput=str(input("What do you want to do? "))
pro=a*b*c
sum=a+b+c
difference=a-b-c
if (userinput == "product"):
    print(f" Your result is {pro}")
elif(userinput=="sum"):
    print(f"Your result is {sum}")
elif(userinput=="difference"):
    print(f"Your result is { difference}")
else:
    print("This operation can't be performed")

# while True:
#     print(sum,end ="")
#     g=str(input("Enter q to stop"))
#     if g=="q":
#         break