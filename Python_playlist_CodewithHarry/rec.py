def a(n):
    f=1
    for i in range(n):
        f=f*(i+1)
    return f 
d=int(input("Enter a number"))
print(a(d))