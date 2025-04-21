num=int(input("Enter the Number:"))
if num>=1500 and num<=2500:
    if num%3==0 and num%5==0 and num%7==0:
        print("Divisible")
    else:
        print("Not Divisible")
else:
    print("Not a Valid Number")
    
    

num=1500
while num<=2500:
    if num%3==0 and num%5==0 and num%7==0:
        print(num)
    num+=1
    
a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
if a<b:
    print("b is maximum number")
else:
    print("a is a maximum number")

x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))
if x<y:
    print("y is the maximum number")
elif y<z:
    print("z is the maximum number")
elif z<x:
    print("x is the maximum number")
else:
    print ("y is the maximum number")

number=int(input("enter the number:"))
if number>0:
    print("positive")
elif number<0:
    print("negative")
else:
    print("zero")
    
tri1=int(input("enther the triangle 1:"))
tri2=int(input("enter the triangle 2:"))
tri3=int(input("enter the triangle 3:"))
if tri1+tri2+tri3==180:
    print("triangle is valied")
else:
    print("Not valied")
    
s=int(input("enter the grossprofit:"))
k=int(input("enther the netprofit:"))
if k>s:
    print("profit")
else:
    print("loss")
    
salary=int(input("enter the basic salary:"))
if salary<=10000:
    hra=salary*(20/100)
    da=salary*(80/100)
    grosssal=hra+da+salary
        
                
x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))

if x>y and x>z:
    print(f'{x} is a greater')
elif y>x and y>z:
    print(f'{y} is a greater')
elif z>x and z>y:
    print(f'{z} is a greater')


name=input("Enter the Name:")
for x in name:
    print(x,'-',ord(x),'-',chr(ord(x)))

m=int(input("Enter the Number"))
for x in range(1,11,1):
    print(x,'X',m,'=',x*m)
    
k=int(input("enter the number:"))
for x in range(1,k+1,1):
    print(x*x*x)
    
n=int(input("enter the n:"))
for x in range(n,0,-2):
    print(x)

n=int(input("enter the n:"))
while n>0:
    if n%2==0:
        print(n)
    n-=2

name=input("enter the name:")
for x in range(len(name)):
    if(x%2==0):
        print(name[x])
        
number=input("enter the num:")
for x in range(x//10):
    print(x)
       

    
