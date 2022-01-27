# # Lambda functions or anonymous
# # def add(a ,b ):
# #     return a+b

# minus= lambda x,y:x-y
# a=2
# b=3
# c=minus(2,3)
# print(c)

def a_first(a):
    return a[0]and a[1]

a=[[1,4],[5,6],[0,23],]
a.sort(key=lambda x:x[1])
print(a)