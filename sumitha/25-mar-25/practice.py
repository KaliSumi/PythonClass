# i=1
# for c in range(1,6,1):
#     for r in range(1,c+1,1):
#         print("*",end=" ")
#     print()
#     i+=1
# i=1
# for r in range(1,6,1):
#   for c in range(1,5,1):
#     print("*",end=" ")
#   for space in range(1,r,-1):
#         print("-",end=" ")
#   print()
#   i+=1
        
# r=0
# for r in range(1,7,1):
#     for c in range(1,6,1):
#         if r==2 and c==2 or r==2 and c==3 or r==2 and c==4 or r==3 and c==2 or r==3 and c==3 or r==3 and c==4:
#             print(" ",end=" ")  
#         elif r==4 and c==2  or r==4 and c==3 or r==4 and c==4 or r==5 and c==2 or r==5 and c==3 or r==5 and c==4:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()
#     r+=1

# x=0
# for x in range(5,0,-1):
#     for y in range(1,x,1):
#         print(y,end=" ")
   
#     print()
#     x+=1




# for r in range(0,6,1):
#     for space in range(5,r,-1):
#         print(" ",end=" ")
#     for c in range(1,r+1,1):
#         print(r,end=" ")
#     print()
# for r in range(4,0,-1):
#     for c in range(1,r+1,1):
#         print("*",end=" ")
#     print()
    

# for r in range(5,0,-1):
#     for space in range(5,r,-1):
#         print(" ",end=" ")
#     for c in range(1,r+1,1):
#         print("*",end=" ")
#     print()


# for r in range(1,6,1):
#     for c in range(1,6,1):
#         if r==1 or c==1 or r==5 or c==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for r in range(1,6,1):
#     for c in range(1,11,1):
#         if r==1 and c==5 or r==2 and c==4 or r==2 and c==6 or r==3 and c==3 or r==3 and c==7 or r==4 and c==2 or r==4 and c==8:
#             print("*",end=" ")
#         elif r==5 and c==1 or r==5 and c==3 or r==5 and c==5 or r==5 and c==7 or r==5 and c==9:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for r in range(1,6,1):
#     for c in range(1,11,1):
#         if r==1 and c==5 or r==2 and c==4 or r==2 and c==6 or r==3 and c==3 or r==3 and c==7 or r==4 and c==2 or r==4 and c==8:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
# for r in range(10,0,-1):
#     for c in range(10,0,-1):
#         if r==1 and c==5 or r==2 and c==4 or r==2 and c==6 or r==3 and c==3 or r==3 and c==7 or r==4 and c==2 or r==4 and c==8:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    


# for x in range(1,6,1):
#     for space in range(5,x,-1):
#         print(" ",end=" ")
#     for y in range(1,6,1):
#         print("*",end=" ")
#     print()

# for x in range(1, 6):
#     print(" " * (5 - x), end="")
#     for y in range(1, x + 1):
#         if y == 1 or y == x or x == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

for r in range(1,8,1):
    for c in range(1,9,1):
        if r==1 or c==1 or r==7 or c==8:
            print("*",end=" ")
        elif r==2 and c==2 or r==2 and c==3 or r==2 and c==6 or r==2 and c==7 or r==2 and c==8 or r==3 and c==2 or r==3 and c==7:
            print("*",end=" ")
        elif r==5 and c==2 or r==5 and c==7 or r==6 and c==2 or r==6 and c==3 or r==6 and c==6 or r==6 and c==7:
            print("*",end=" ")
        else:
            print("1",end=" ")
    print() 

row=int(input("Enter The Row:"))
for r in range(row,0,-1):
    for c in range(0,r,1):
        print("*",end=" ")
    for space in range(row,r,-1):
        print(" ",end="   ")
    for c in range(0,r,1):
        print("*",end=" ")
    print()
for r in range(0,row,1):
    for c in range(0,r+1,1):
        print("*",end=" ")
    for space in range(row,r+1,-1):
        print(" ",end="   ")
    for c in range(0,r+1,1):
        print("*",end=" ")
    print()

for x in range(1,5,1):
    print("  "*(5-x),end="")
    for y in range(x,0,-1):
        print(y,end=" ")
    for y in range(2,x+1,1):
        print(y,end=" ")
    print()

for x in range(1,6,1):
    for y in range(1,x+1,1):
        print("#",end=" ")
    print()

for x in range(1,6,1):
    for space in range(5,x,-1):
        print("",end=" ")
    for y in range(1,x+1,1):
        print("#",end=" ")
    print()

for x in range(1,5,1):
    for space in range(4,x,-1):
        print("",end=" ")
    for y in range(1,x+1,1):
        print("#",end=" ")
    for space in range(5,x,-1):
        print(" ",end=" ")
    for y in range(5,x+1,1):
        print("#",end=" ") 
    print()


for x in range(1,5,1):
    for space in range(1,x,1):
        print(" ",end="")
    for y in range(x,5,1):
        print(y,end=" ")
    print()
for x in range(3,0,-1):
    for space in range(1,x,1):
        print(" ",end="")
    for y in range(x,5,1):
        print(y,end=" ")
    print()
  
