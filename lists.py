from re import S


grocery=["Harpic","Vim Bar","Graphic card",69]
print(grocery[0])
num=[2,7,9,11,3]
print(num[2])
print(num.sort())
print(num)

print(num[1:4:2])
print(max(num))
num.append(1)
num.append(69)
num.append(69)
num.append(69)
num.insert(1,88)
print(num)
num.remove(69)
print(num)





num[2]=999999
print(num)

s=1
b=2
s,b=b,s
print(s,b)
a=[2,1]
a.reverse()
print(a)
