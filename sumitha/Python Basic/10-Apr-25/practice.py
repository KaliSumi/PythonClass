def fun(letter):
    inp=input("Enter the Sentence")
    print(inp.count(letter))

fun(input("Enter the Letter:"))

Alpha=[1,2,3,4,5]
number=['a','b','c','d','e']
di={}
def fun1(a,n):
    for x,y in zip(a,n):
        di[x]=y
    print(di)
fun1(Alpha,number)

# from math import *
import math
def Armstrong(para):
    r=str(para)
    l=len(r)
    f=0
    for x in r:
        f=f+int(pow(int(x),l))
    print("Armstrong Number" if para == f  else "not a Armstrong number")
Armstrong(150)

l=[9,5,7,4,8,2]

l.sort()
print(l)

a=[1,2,3,4,5,6,6,9,2,4,5]
a.remove(6)
a.remove(4)
a.remove(5)
a.remove(2)
print(a)








