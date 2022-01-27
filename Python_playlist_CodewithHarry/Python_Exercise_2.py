# Faulty calculator
# 45*3=555,56+9=77,56/6 =4
x=int(input("Enter your first number"))
y=int(input("Enter your Second number"))
A=("What kind of operation you wanna perform? Options are as follow:-")
print(A)
B='''
For addition Enter'+'
For subtraction Enter'-'
For multiplication '*'
For division '/'
'''
print(B)
d=45*3
e=56+9
f=56/6
q=x+y
r=x-y
s=x*y
t=x/y
z=input("Enter operation you wannna perform")
if s==d:
    print("555")
elif q==e:
    print("77")
elif t==f:
    print("4")
elif z=='+':
    print(q)
elif z=="-":
    print(r)
elif z=="*":
    print(s)
elif z=="/":
    print(t)
a=open
with open("Raunak.txt") as z:
    print(z.read())

