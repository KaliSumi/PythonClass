# num=[]
# s=0
# no=int(input("enter the num:"))
# for i in range(0,no,1):
#     num.append(int(input(f"enter the num{i+1}:")))
# for i in num:
#     if i>0:
#         s=s+i
# r,t=0,1
# if s%2==0:
#     for x in str(s):
#         r=r+int(x)
#     print(r)
# else:
#     for x in str(s):
#         t=t*int(x)
#     print(t)



# print()

# W=['THE','APTECH','LEARNING']
# for x in range(0,len(W),1):#0,1,2
#     W[x]=W[x][::-1]
# print(W)


# h="Muthu"
# print(h[0:2])
# print(h[::-1])

# name=['ram','raju','ravi']
# s=" ".join(name)
# print(s)

s=[]
n=int(input("enter the num:"))
for n in range(1,n,1):
    x=65
    while x<=65:
        if s%2==0:
            print(chr(x))
        x+=1
    #     while y<1:
    #         y+=1
    # x+=1
    # print(s)

# data=[]
# n=int(input("Enter the Number:"))
# a,d=65,1
# for x in range(0,n,1):
#     if x%2==0:
#         data.append(chr(a))
#         a+=1
#     else:
#         data.append(d)
#         d+=1
# print(data)

# n=input("enter the name:")
# s,c=1,0
# while s<len(n):
#     if n[s]=="a" or n[s]=="e" or n[s]=="i" or n[s]=="o" or n[s]=="u":
#         c+=1
#     s+=1
# print(c)

n=[]
vow=['a','e','i','o','u']
k=int(input("enter the no:"))
for x in range(0,k,1):
    n.append(input(f"enter the name{x+1}:"))

vo=[]
for x in range(0,k,1):
    vo.append(0)
    for y in n[x]:
        if y in vow:
            vo[x]+=1

for x in range(0,len(n),1):
    print(f'{n[x]}-{vo[x]}')

        
# row=int(input("Enter The Row:"))
# for r in range(row,0,-1):
#     for c in range(0,r,1):
#         print("*",end=" ")
#     for space in range(row,r,-1):
#         print(" ",end="   ")
#     for c in range(0,r,1):
#         print("*",end=" ")
    # for x in range(1,7,1):
    #     for space in range(r,x,-1):
    #         print("",end=" ")
    #     for y in range(1,x+1,1):
    #         print(y,end=" ")

#     print()
# for r in range(0,row,1):
#     for c in range(0,r+1,1):
#         print("*",end=" ")
#     for space in range(row,r+1,-1):
#         print(" ",end="   ")
#     for c in range(0,r+1,1):
#         print("*",end=" ")
#     print()