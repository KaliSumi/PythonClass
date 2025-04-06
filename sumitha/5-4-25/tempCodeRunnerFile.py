for r in range(5,0,1):
    for space in range(0,r,-1):
        print(" ",end=" ")
    for c in range(1,r+1,1):
        print("*",end=" ")
    print()