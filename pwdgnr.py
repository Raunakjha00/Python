import random
import turtle
# a='QWERTYUIOPASFDGHJKLZXCVBNM'
# B='qerwtyuiopsadfghjklzxvbnm'
# c='_-=@#!$%^&'
# d='0123456789'
# e=a+B+c+d
# print(f' This is a suggested strong password for you {"".join(random.sample(e,12))}')
c=input("Enter q to Roll the dice")
# t = turtle.Turtle()
# t.fillcolor('orange')
# t.begin_fill()
# t.circle(1)
# t.end_fill()
# print(t)
w=''' ______________
|              |
|              | 
|      .       | 
|              | 
|______________|
                '''
e=''' ______________
|              |
|              | 
|     . .      | 
|              | 
|______________|
                '''
r=''' ______________
|              |
|              | 
|      . . .   | 
|              | 
|______________|
                '''
t=(''' ______________
|              |
|      .  .    | 
|      .  .    | 
|              | 
|______________|''')
y=''' ______________
|              |
|      .  .    | 
|      .  .    | 
|        .     | 
|______________|'''
u=''' ______________
|              |
|    .  .  .   | 
|    .  .  .   | 
|              | 
|______________|'''
if c=='q':
    a= random.randint(1,6)
    if a==1:
        print(w)
    elif a==2:
        print(e)
    elif a==3:
        print(r)
    elif a==4:
        print(t)

    elif a==5:
        print(y)
    elif a==6:
        print(u)
else:
     pass       
