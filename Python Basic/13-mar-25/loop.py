# # name=input("enter the name:")
# # if name.isalpha():
# #     x=name
# #     i=0
# #     s=0
# #     while i<len(name):
# #         print(x[i],"-",(ord(x[i])))
# #         s=s+ord(x[i])
# #         i=i+1
# #     print(s)
# # else:
# #     print("invalied input")

# # name=input("enter the name:")
# # s=0
# # if name.isalpha():
# #     x=name
# #     for x in name:
# #         print(x,'-',ord(x))
# #         s=s+ord(x)
# #     print(s)
# # else:
# #     print("Incorrect Input")

# for x in range(1,10,1):
#     print("Times",x)

# for x in range(0,10,1):
#     print("Times",x)


# num=int(input("Enter the Number:"))
# if num>0:
#     for x in range(1,num,1):
#         print(x)
# else:
#     print("Only Positive Number is Accepted")

# for x,y in zip(range(10,0,-1),range(1,11,1)):
#     print(x,y)

# for x in range(0,11,1):
#     a=10-x
#     b=x+1
#     print(a,b)

# s=input("Enter the Name:")
# for x in s:
#     print(x)


# s=input("Enter the Name:")
# co=len(s)
# for x in range(0,co,1):
#     if x%2!=0:
#         print(s[x])


# s=int(input("Enter the Number"))
# match s%2==0:
#     case True:
#         print("+ive")
#     case _:
#         print("-ive")

# month=int(input("enter month"))
# match month:
#     case 1:
#         print("30 days")
#     case 2:
#         print("28 days")
#     case 3:
#         print("31 days")
#     case 4:
#         print("30 days")
#     case 5:
#         print("30 days")
#     case 6:
#         print("31 days")
#     case 7:
#         print("30 days")
#     case 8:
#         print("31 days")
#     case 9:
#         print("30 days")
#     case 10:
#         print("31 days")
#     case 11:
#         print("30 days")
#     case 12:
#         print("31 days")

# num=int(input("enter the num"))
# match num%2!=0:
#     case True:
#         print("odd number")
#     case _:
#         print("even number")


x=int(input("enter the natural numbers"))
count =1
while count < 11:
    print(count)
    count = count + 1
for x in range(11):
    print(x)
i=0
for x in range(1,5,1):
    x=i+1
    print(x,i)

    
row = 10
for x in range(1, row + 1, 1):
    for y in range(1, x + 1):
        print(y, end=' ')
    print("")

x=0
y=int(input("enter the number:"))
for x in range(1,y+1,1):
    print(x)
x+=y

