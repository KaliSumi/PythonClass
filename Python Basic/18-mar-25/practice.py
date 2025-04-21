# for x in range(65,69,1):
#     for space in range(69,x,-1):
#         print(' ',end='')
#     for y in range(65,x+1,1):
#         print(chr(x),end=" ")
#     print()
# for x in range(100,96,-1):
#     for space in range(100,x,-1):
#         print(end=' ')
#     for y in range(97,x+1):
#         print(chr(x),end=' ')
#     print()


# r=0
# i=1
# while i<=5:
#         j=1
#         while j<=5:
#             if i==1 and j==1 or i==1 and j==5 or i==5 and j==1 or i==5 and j==5 or i==3 and j==3:
#                 print("$",end=' ')
#             else:
#                 print(" ",end=" ")
#             j+=1
#         print()
#         i+=1

# row=int(input("Enter the No.of.Rows"))

# if row%2!=0:
#     i=1
#     while i<=row:
#         j=1
#         while j<=row:
#             if i==1 and j==1 or i==row and j==row or i==1 and j==row or i==row and j==1 or i==row//2+1 and j==row//2+1:
#                 print("$",end=" ")
#             else:
#                 print(" ",end=" ")
#             j+=1
#         print()
#         i+=1
# else:
#     print("Invalid input")

# row=int(input("Enter the Rows:"))
# if row%2!=0:
#     s=1
#     while s<=row:
#         k=1
#         while k<=row:
#             if s==1 and k==2 or s==1 and k==row-1:
#                 print("0",end=' ')
#             elif s==row and k==2 or s==row and k==row-1:
#                 print("$",end=' ')
#             elif s==row//2+1 and k==row//2+1:
#                 print("A",end=' ')
#             else:
#                 print(" ",end=' ')
#             k+=1
#         print()
#         s+=1


# row=int(input("Enter The Number"))
# r=1
# while r<=row:
#     c=1
#     while c<=row:
#         if r==1 or r==row or c==1 or c==row:
#             print("$",end=" ")
#         else:
#             print(" ",end=" ")
#         c+=1
#     print()
#     r+=1
# a==1 and b==2 or a==1 and b==3 or a==1 and b==4 or a==1 and b==5 or a==2 and b==1 or a==3 and b==1 and a==4 and b==1:
# row=5
# a=1
# while a<=5:
#     b=1
#     while b<=5:
#         if a==1 and b==1 or a==1 and b==row or a==5 and b==1 or a==5 and b==row:
#             print("0",end=" ")
#         elif b==1 or b==row or a==1 or a==5:
#             print("1",end=" ")
#         else:
#             print(" ",end=" ") 
#         b+=1
#     print()
#     a+=1


# r=5
# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         if i==1 and j==1 or i==2 and j==1 or i==3 and j==1 or i==4 and j==1 or i==5 and j==1 or i==2 and j==5 or i==3 and j==5 or i==4 and j==5 or i==5 and j==5:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
    
    
#     print()
#     i+=1

r=5
a=65

while a<=69:
    b=65
    while b<=69:
        if a==b or a+b==134:
            print(chr(b),end=" ")
         
        else:
            print(" ",end=" ")
    
        b+=1
    print()
    a+=1

