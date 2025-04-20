# name=input("Enter the Name:")
# # c=0
# # for x in name:
# #     c+=1

# for x in range(0,len(name),2):
#     print(name[x])

# n=int(input("Enter the Number:"))#123
# c=0
# while n!=0:#123!=0 12!=0 1!=0 0!=0
#     c=c+1#0+1=1+1=2+1=3
#     n=n//10#123//10 12//10 1//10
# print(c)

# n=int(input("Enter the Number"))#1005
# c=0
# for x in str(n):#'1005'
#     c=c+1
# print(c)

unit=int(input("Enter the Units:"))
if unit>0 and unit<=50:
    amount=unit*0.50
elif unit>50 and unit<=150:
    amount=25+(unit-50)*0.75
elif unit>150 and unit<=250:
    amount=25+75+(unit-150)*1.20
elif unit>250:
    amount=25+75+120+(unit-250)*1.50
totamount=amount+(amount*0.20)
print(totamount)


unit=int(input("Enter the Units:"))
if unit<=50:
    amount=unit*0.50
elif unit>50 and unit<=100:
    amount=unit*0.75
elif unit>100 and unit<=250:
    amount=unit*1.20
else:
    amount=unit*1.50
totamount=amount+(amount*0.20)
print("Amount=",totamount)


#looping 
n=1
while n<10:
    print("Sun")
    n=n+1
print("Thank You")

#1+2+3+4+5=15
#1+2+3+4+5+6+7+8+9+10=55
s=0
n=1
while n<=10:
    s=s+n#0+1=1+2=3+3=6+4=10+5=15+6=21+7=28+8=36+9=45+10=55
    n=n+1
print(s)
print("thankyou")

e,o=0,0
for x in range(1,11,1):
    if x%2==0:
        e=e+x
    else:
        o=o+x

print('Even=',e)
print('odd=',o)

t,f=0,0
x=1
while x<=10:
    if x%3==0:
        t+=1
    elif x%5==0:
        f+=1
    x+=1

print('Five=',f)
print('Three=',t)

s=0
x=1
while x<=25:
    if x%5==0:
        s=s+x
    x=x+1
print(s)

t,f=0,0
x=1
while x<30:
    if x%2==0:
        t=t+1
    else:
        x%5==0
        f=f+1
    x=x+1
print("2 divisiable number:",t)
print("5 divisiable number:",f)



        

    
