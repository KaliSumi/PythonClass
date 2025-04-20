# x=1
# for r in range(0,5,1):
#     for c in range(0,r+1,1):
#         print(x,end=" ")
#         x=x+2
#     print()


x=29
for r in range(5,0,-1):
    for c in range(0,r,1):
        print(x,end=" ")
        x=x-2
    print()


# for x in range(1,6,1):
#     if x%2==0:
#         for y in range(5,0,-1):
#             print(y,end=" ")
#     else:
#         for y in range(1,6,1):
#             print(y,end=" ")
#     print()


for x in range(1,6,1):
    for z in range(5,x,-1):
        print("-",end=" ")
    for y in range(1,x+1,1):
        print("&",end=" ")
    print(x,end=" ")
    for y in range(1,x+1,1):
        print("&",end=" ")
    print()

x=5
for r in range(1,6,1):
    for c in range(1,r+1,1):
        print(c*5,end=" ")
    print()

x=20
for r in range(6,0,-1):
    for c in range(1,r,1):
        print(c*5,end=" ")
    print()

x=5
for r in range(6,0,-1):
    for c in range(1,r,1):
        print(r*5,end=" ")
    print()

r=1
while r<=5:
    space=5
    while space>r:
        print(" ",end=" ")
        space-=1
    c=1
    while c<=r:
        print("&",end=" ")
        c+=1
    print(r,end=" ")
    c=1
    while c<=r:
        print("&",end=" ")
        c+=1
    print()
    r+=1
