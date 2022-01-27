# a=input("Enter a number")
# b=input("Enter a number")
# c=input("Enter a number")
# a=int
# a=int(a)
# b=int(b)
# c=int(c)

'''From here'''

a = int(input("enter any number:"))
b = int(input("enter any number:"))
c = int(input("enter any number:"))

if (type(a) == int):
    print("First number check ! Accomplished.You may continue")
else:
    print("Plz enter valid number in first input area")
if (type(b) == int):
    print("Second number check ! Accomplished. You may continue ")
else:
    print("Plz enter valid number in second input area. You may continue")
if (type(c) == int):
    print("Third number check ! Accomplished. You may continue")
else:
    print("Plz enter valid number in third input area")

# z=( "Options are "+"product","sum","difference")
# print(z)

'''i have used dictionary instead of
# z=( "Options are "+"product","sum","difference")
# print(z) --> this line of code 
'''
z = {
    "options": "following",
    "add": "+",
    "sub": "-",
    "pro": "*",
}
za = print(z.items())
userinput = str(input("What do you want to do? "))
pro = a * b * c
add = a + b + c
diff = a - b - c
"""here in diff there was a little mistake i have fixed it"""

# you don't need to put parenthesis in codes of if statement. its
# optional 🙂 #

if userinput == "pro":
    print(f" Your result is {pro}")
elif userinput == "add":
    print(f"Your result is {add}")
elif userinput == "diff":
    print(f"Your result is {diff}")
else:
    print("Sorry!This operation can't be performed")
