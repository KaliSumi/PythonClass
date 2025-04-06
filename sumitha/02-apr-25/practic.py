# i=1
# while True:
#     i+=1
#     if i>10:
#         break
# print("thank you")

# for x in range(1,11,1):
#     if x==3 or x==5:
#         continue
#     print(x)
# print("thankyou")

# for x in range(1,11,1):
#     if x%2==0:
#         pass
#     print(x)
# print("thankyou")

# mark=[15,25,45,78,85]
# i=0
# while i<5:
#     print(mark[i]+15)
#     i+=1
# for x in range(0,5,1):
#     print(mark[x]*2)
# for x in mark:
#     print(x*2,end=" ")

# a=[10,20,30,40,50]
# total=sum(a)
# print(total)

# a=[1,2,3,4,5]
# for x in a:
#     print(x**2)

s=[10,20,30,20,40,30,50,60,20,70]
for x in s:
    if x==20 or x==30:
        s.remove(x)
print(s)

s=[10,20,30,20,40,50,40]
s.remove(20)
s.remove(40)
print(s)


# a=[1,2,3,4,5]
# b=[4,5,6,7,8,9,10]
# a.extend(b)
# a.remove(4)
# a.remove(5)
# print(a)

# matA=[]
# temp=[]
# c=0
# row=int(input("enter the num of row:"))
# col=int(input("enter the num of col:"))
# for x in range(row):
#     for y in range(col):
#         temp.append(int(input(f"enter the num[{x},{y}]:")))
#     matA.append(temp)
#     temp=[]
# for x in range(0,row,1):
#     for y in range(0,col,1):
#         if x==y:
#             matA[x][y]*=2
# s=[0,0,0]
# for x in range(0,len(matA),1):
#     for y in range(0,len(matA),1):
#         s[x]=s[x]+matA[x][y]#2+2=4+3=7
#         print(matA[x][y],end=" ")
#     print()
# print(s)