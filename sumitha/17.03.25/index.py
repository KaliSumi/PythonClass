# name=input("enter the name:")
# n=0
# s=''
# while n<len(name):
#     if name[n]>='a'and name[n]<='z':
#         s+=name[n].upper()
#     elif name[n]>='A' and name[n]<='Z':
#         s+=name[n].lower()
#     n+=1
# print(s)

# row=0
# while row<5:
#     col=0
#     while col<5:
#         print(col,end=" ")
#         col+=1
#     print()
#     row+=1

# row=0
# while row<5:
#     col=0
#     while col<5:
#         print(row,end=" ")
#         col+=1
#     print()
#     row+=1


# row=0
# while row<5:
#     col=0
#     while col<5:
#         print('(',row,col,')',end=" ")
#         col+=1
#     print()
#     row+=1


# i=1
# while i<=5:
#     print(i,end=" ")
#     j=1
#     while j<=5:
#        if j%2==0:
#             print(j,end=" ")
#        j+=1
#     k=65
#     while k<=69:
#         if k%2==0:
#             print(chr(k),end=" ")
#         k+=1
#     print()
#     i+=1

# for x in range(0,5,1):
#     for y in range(0,5,1):
#         print(y,end=" ")
#     print()
 
 
# for x in range(0,5,1):
#     for y in range(0,5,1):
#         print(x,end=" ")
#     print()


# for x in range(0,5,1):
#     for y in range(0,5,1):
#         print(x,y,end=" ")
#     print()


# for x in range(0,5,1):
#     print(x,end=" ")
#     for y in range(0,5,1):
#        print(y,end=" ")
#     print()

# for x in range(0,5,1):
#     print(x,end=" ")
#     for y in range(0,5,1):
#        print(y,end=" ")
#     for z in range(65,70,1):
#         print(chr(z),end=" ")
#     print()


# for x in range(0,5,2):
#     print(x,end=" ")
#     for y in range(0,5,2):
#        print(y,end=" ")
#     for z in range(66,70,2):
#         print(chr(z),end=" ")
#     print()


row=0
while row<5:
    if row==ord(36):
        col=0
        if col==ord(36):
            while col<5:
                print(row,col,end=" ")
        col+=1
    print()
    row+=1


# row=0
# while row<5:
#     col=0
#     while col<5:
#         if col%2!=0:
#          print(col,end=" ")
#     col+=1
#     print()
#     row+=1

row=0
while row<5:
    col=0
    while(col<5):
        if(col%2==0):
            print("0",end="")
        else:
             print("1",end="")
        col+=1
    print()
    row+=1
   
row=0
while row<5:
    col=0
    while(col<5):
        if(row%2==0):
            print("1",end="")
        else:
             print("0",end="")
        col+=1
    print()
    row+=1

for x in range(36,1):
    print(chr(x),end=" ")
   
    