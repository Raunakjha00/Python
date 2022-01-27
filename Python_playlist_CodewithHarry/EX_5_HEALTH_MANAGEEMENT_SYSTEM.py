#Health Management System
# Clients-Harry,Rohan,Hammad
# write a function that when executed 
def getdate():
    import datetime
    return datetime.datetime.now()
a=int(input("enter 1 for Harry \n 2 for Rohan \n 3 for Hammad \n"))
if a==1:
    
    b=int(input("Enter 1 for exercise and 2 for food \n"))
    if b==1:
        with open("Harry-ex.txt","a")as op:
            op.write( input("What exercise you did today?"))
        
    elif b==2:
        with open ("Harry-food.txt","a")as op:
            op.write( input("Enter food you ate today"))
            
elif a==2:
    c=int(input("Enter 1 for exercise and 2 for food \n"))
    if c==1:
         with open("Rohanex.txt","a")as op:
            op.write( input("Enter exercise you did today Rohan "))
    elif c==2:
        with open ("Rohan-food.txt","a")as op:
            op.write( input('Enter food u ate today Rohan ') )
elif a==3:
    d=int(input("Enter 1 for exercise and 2 for food \n"))
    if d==1:
        with open ("Hammad-ex.txt","a")as op:
            op.write( input("Enter Exercise you did today Hammad ") )
    elif d==2: 
        with open ("Hammad-food.txt","a")as op:
            op.write ( input("Enter food you ate today Hammad "))