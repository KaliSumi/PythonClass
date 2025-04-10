def name():
    k=input("enter the name:")
    print(k,end=" ")

name()
print("world!")

def sum(a,b):
    result=a+b
    return result

input=sum(5,4)
print(input)

def add():
    s=int(input("enter the number:"))
    if s%2==0:
        print("its a even number")
    else:
        print("its a odd number")

add()

def num(a,b,c):
    r=0    
    if a>b and a>c:
        r=a
    elif b>a and b>c:
        r=b
    else:
        r=c
    return r
print(num(int(input("a=")),int(input("b=")),int(input("c="))),"is a greater number")


from math import*
a=int(input("enter the num:"))
print(factorial(a))

def num(a,b):
    print("add",'-',a+b)
    print("sub",'-',a-b)
    print("mul",'-',a*b)
    print("div",'-',a/b)
a=int(input("Enter the values of a"))
b=int(input("Enter the values of b"))
num(a,b)

from string import*
vo=['a','e','i','o','u']
c=0
def k():
    global c
    inp=input("Enter the Sentences:")
    for x in inp:
        if x in vo:
            c=c+1
    print(c)
k()

s=input("enter the word:")
if s.lower()==s[::-1].lower():
    print("its a palindrom")
else:
    print("its not a palindrom")

def res():
    inp=int(input("enter the number"))
    return inp[::-1]
# print(res)
l=['Ram','Cat','James']
def name():
    le=[]

    for x in l:
        le.append(len(x))
    return le

for x,y in zip(l,name()):
    print(x,y)

def ce():
    c=int(input("enter the value:"))
    print(c*(9/5)+32)
ce()

def fi():
    a, b = 0, 1
    sequence = []
    for x in range(5):
        sequence.append(a)#0 1 1 2 3
        a, b = b, a + b # 2,3
    print(sequence)        
fi()
