# from ossaudiodev import SNDCTL_DSP_SPEED


from re import X


l=10






# def function1(n):
#     # l=2
#     m=3
#     global l
#     l=l+21
#     print(l,m)
#     print(n,"i Have printed")
# function1("This is me")





x=89
def harry():
    x=20
    def rohan():
        global x 
        x=88
        print(x)
        rohan(33)
        print("After calling rohan()",x)
harry()
print(x)
# rohan()
print(x)
q=' Rauank jha  '
print(q.strip())