a=input("Are you ready for quiz:-")
questions=1
right_answer=0
wrong_answer=0
if "yes" in a.lower():
    while questions<=3:
        print("Which is the Tallest building of the world?")
        b=input("Enter your answer")
        
        if "burj khalifa"in b.lower():
            print("Correct answer")
            right_answer+=1
            questions=questions+1
            
        else:
            print("Wrong Answer The correct one is Burj Khalifa")
            wrong_answer+=1
            questions=questions+1
            
        
        print("Who is the richest person in the world at the current time?")
        c=input("Enter your answer")
        
        if "elon musk"in c.lower():
            print("Correct answer")
            right_answer+=1
            questions=questions+1
            
        else:
            print("Wrong Answer The correct one is Elon musk")
            wrong_answer+=1
            questions=questions+1
            
        print("What is the name of tallest hotel")
        d=input("Enter your answer")
        
        if "burj al arab" in d.lower():
            print("Correct Answer")
            
            right_answer=right_answer+1
            questions=questions+1
        else:
            print("The right answer is Burj Al Arab")
            questions=questions+1
            wrong_answer=wrong_answer+1
else:
    pass
print(f'You said total {right_answer} right answers and you got {right_answer*10} points')
print(f'You said total {wrong_answer} wrong answers ')
        