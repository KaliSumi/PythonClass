# row=6
# for x in range(1,row,1):
#     for y in range(x+1):
#         print(y,end=" ")
#     print()

# r=6
# x=1
# while x<=r:
#     c=1
#     while c<=r:
#         print(c,r-1,end=" ")
        
#         c+=1
#     print()
#     x+=1

# row=1
# while row<=5:
#     col=1
#     while col<=5:
#         if (row%2==0):
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#         col+=1
#     print()
#     row+=1

row=0
while row<5:
    col=0
    while col<5:
        print(col,end=" ")
        col+=1
    print()
    row+=1


# row=0
# while row<5:
#     col=0
#     while col<5:
#         print(row,end=" ")
#         col+=1
#     print()
#     row+=1

# i=1
# while i<=5:
#     print(i,end=" ")
#     j=1
#     while j<=5:
#         if j%2==0:
#             print(j,end=" ")
#         j+=1
#     k=65
#     while k<69:
#         if k%2==0:
#             print(chr(k),end=" ")
#         k+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print("$",end=" ")
#         j+=1
#     print()
#     i+=1
# row=65
# while row<70:

#     col=65
#     while col<70:
#         print(chr(row),end=" ")
#         col+=1
#     print()
#     row+=1



# col=70
# for x in range(65,col,1):
#     for y in range(x+1):
#         print(chr(y),end=" ")
#     print()

# r=3
# i=0
# while i<r:
#     j=0
#     while j<i:
#        if j%2==0:
#          print(" ",end=" ")
#        else:
#          print("$",end=" ")
#        j+=1
#     print()
#     i+=1
row=6
for x in range(1,row,1):
    for y in range(x+1):
        print(x,end=" ")
    print()

