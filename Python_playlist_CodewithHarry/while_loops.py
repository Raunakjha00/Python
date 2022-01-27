# i=0
# while i<45:
#     print(i)
#     i=i+1
# a= int(input("Enter a number"))
# s=1
# while s<11:
#     print(f"{a} x {s} = {a*s}")
#     s=s+1
import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?1234567890"
p =  "".join(random.sample(s,passlen ))
print (p)
