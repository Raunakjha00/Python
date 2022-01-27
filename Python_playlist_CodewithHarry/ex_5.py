#Health Management System
# Clients-Harry,Rohan,Hammad
# write a function that when executed 
def getdate():
    import datetime
    return datetime.datetime.now()
a=int(input("enter 1 for Harry \n 2 for Rohan \n 3 for Hammad"))
if a==1:
    
    b=int(input("Enter 1 for exercise and 2 for food"))
    if b==1:
        with open ("Harry-ex.txt","a")as op:
            op.write(input( "Enter exercise you did today \n. \n" ))
    elif b==2:
        with open ("Harry-food.txt","a")as op:
            g=input("Enter food you ate today. \n")
            op.write(f'{g }\n' )
elif a==2:
    c=int(input("Enter 1 for exercise and 2 for food \n"))
    if c==1:
         with open("Rohan-ex.txt","a")as op:
            op.write( input("Enter exercise you did today Rohan ,end=' '"))
            
    elif c==2:
        with open ("Rohan-food.txt","a")as op:
            op.write( input('Enter food u ate today Rohan ,end=" "') )
elif a==3:
    d=int(input("Enter 1 for exercise and 2 for food \n"))
    if d==1:
        with open ("Hammad-ex.txt","a")as op:
            op.write( input("Enter Exercise you did today Hammad ,end=" "") )
    elif d==2: 
        with open ("Hammad-food.txt","a")as op:
            op.write ( input("Enter food you ate today Hammad,end=" " "))