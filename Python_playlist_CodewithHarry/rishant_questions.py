#  question no.1
a=float(input("Enter a number \n"))
b=float(input("Enter another number \n"))
c=a+b
while (c>(1-a+b)):
    print(c)
    
    d=input("Press q to stop \n")
    # continue
    if d=="q":
        break
    while d == "q":
        break
    else:
        continue

#     # else:
#         # continue 

# question no.2
a=input("Enter your name \n")
b=input("Enter your Address \n")

while True:
    c=input("Enter your phone number \n")
    if len(c)==10:
        
        break
    else:
        print("Enter a valid number")
        continue

    print("Enter valid phone number")

d=input("Enter your email address \n")
e=input("Enter your hobby")
f={
    "Your name is":a,
    "Your Address is":b,
    "Your Phone number is":c,
    "Your Email aaddress is":d,
    "Your hobby is ":e
}

print(f)

# print(f.keys())
# print(f.values())


# question no.3
a=input("Enter a comment \n")
if "Python" in a:
    print("It is being talked about python")
else:
    pass
# question no.4
z=input("Enter name of first student")
y=input("Enter name of second student")
print(z+y)

# question no.5
# I don't know about repel but i can print table of 5 using loop
# e=5
# s=1
# while s<11:
#     print(f"{e} x {s}={e*s}")
#     s=s+1
# Sum = 0
# While(True):
# userInput = input('enter a number : ')
# if (userInput != sum = sum+int(userInput))
# Else:
#     print('''thanks for checking us out''')

#     pass
