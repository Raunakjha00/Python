#create a dictionary and take input from user and return the word from the dictionary
#It is a Hindi to English dicitionary
a={"Padhai":"Study",'Kitab':'Study',"Chalna":"To walk","Sona":"To sleep"}
b="Options for you  are as follow"
print(b+" ")
print(a.keys())
c=str(input("Enter a word from options\t"))
if c in a:
    print("The meaning of your word is as follow")
else:
    print("Sorry! for your inconvience We are unable to find word you searched we will soon add word you searched ")

print(a.get(c))