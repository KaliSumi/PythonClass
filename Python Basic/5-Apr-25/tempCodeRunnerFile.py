for r in range(1,6,1):
    for space in range(5,r,-1):
        print(" ",end=" ")
    for c in range(1,r+1,1):
        print("*",end=" ")
    print()
