# # list1=[["Harry",1],["Larry",4],["Carry",22],["Marry",29]]
# # dict1=dict(list1)
# # for i,z in dict1.items():
# # list2= [["Harry",11],["Larry",12],["Carry",44],["Marry",22]]
# #     z=str(z)
# #     print(i+"Eats "+ z +" Lollipops a day")
# list1=[["Harry",11],["Larry",12],["Carry",44],["Marry",22]]
# dict1=dict(list1)
# dict1=dict(list1)
# print(dict1)
# for  item in dict1:
#      print(item)
# for item,lollipop in list1:
#     print(item, lollipop)
#     # quick quiz
 

# for item in l:
#     if( type(item)==int and item <6):
#         print(int)
items=["Harry","Raunak",2,3,4,5,67,53,33,654,65,]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)
