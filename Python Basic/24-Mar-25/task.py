# i=0
# for x in range(0,9,2):
#     for y in range(0,x+1,1):
#         print("*",end=" ")
#     print()
     
# i=0
# for x in range(1,6,1):
#     for space in range(5,x,-1):
#         print(" ",end=" ")
#     for y in range(1,x+1,1):
#         print(x,end=" ")
#     for z in range(65,70,1):
#         print(chr(z),end=" ")

#     for y in range(1,x+1,1):
#         print(x,end=" ")
  
#     print()      


# list()
# name=[]
# no=int(input("enter the no name:"))
# for x in range(0,no,1):
#     name.append(str(input(f"enter the name{x+1}:")))
# print(name)

name=[]
no=int(input("enter the no name:"))
for x in range(0,no,1):
    y=str(input(f"enter the name{x+1}:"))
    if len(y)>=5:
        name.append(y)
    else:
        print("INVALID NAME")

print(name)

