from math import *
r=int(input("Enter the Radius:"))
print("Area of Circle is:",2*pi*(r**2))

z=int(input("enter number"))
print("odd" if z%2!=0 else "even")

s=int(input("enter the num1:"))
k=int(input("enter the num2:"))
j=s+k
z=j*5
print("the num divisiable by 3" if z%3==0 else"not divisiable by 3")

age=int(input("age is:"))
print("vote" if age>=18 else "not")

first_number=int(input("enter the num1:"))
second_number=int(input("enter the num2:"))
third_number=int(input("enter the num3:"))

print(first_number+second_number+third_number if first_number>0 and second_number>0 and third_number>0 else "Only Positive number is accepted") 

a=int(input("enter the num:"))#8 -9
print(a if a>0 else a*-1)

L=int(input("length:"))
B=int(input("breadth:"))
print(2*(L+B))

r=int(input("enter the radius:"))
print("d=",2*r)
print("c=",2*3.14*r)
print("a=",3.14*r*r)