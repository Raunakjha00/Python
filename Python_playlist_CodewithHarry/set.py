s=set()
s_from_list=set([1,2,3,4])
print(s_from_list)
s.add(1)
print(s)
print(s.union((1,2,3)))
print(s)
a=(2,3,4,)
print(s.isdisjoint(a))




# question 

a=int(input("Enter your age"))
if 100>a>7:
    print("You can drive")
elif 0>a>100:
    print("Age you entered is invalid")
else:
    print("Your can't drive")