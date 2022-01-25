# a=2
# b=3
# c=sum([a,b])#built_in function
# print(c)


def function1():
     print("Hello you are in function one")
def function2(a,b):
    '''This is docstring of first function'''
    avg=(a+b)/2
    return avg
v=function2(5,7)
print(v)
print(function2.__doc__)#there are two underscores
