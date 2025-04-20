def num():
   
    m=int(input("enter the number:"))
    for x in range(1,11,1):
            print(x,"*",m,"=",x*m)
num()

def num(table):
      for x in range(1,11,1):
        print(x,"*",table,"=",table*x)

numbers=(int(input(f"enter the number")))
num(numbers)

tab=[]
def num(mul):#5
    for x in range(1,11,1):
         tab.append(f'{x}*{mul}={x*mul}')   
    return tab 
       
inp=int(input("Enter the Number:"))#5
r=num(inp)#5
for x in r:
     print(x)

l=[]
def num():
    inp=int(input("enter the number:"))
    for x in range(1,11,1):
        l.append(f'{x}*{inp}={x*inp}')
    return l
for x in num():
     print(x)

