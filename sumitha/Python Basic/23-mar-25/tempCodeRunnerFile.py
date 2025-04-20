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
