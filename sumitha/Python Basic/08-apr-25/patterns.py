def star(a):
    for x in range(a):
        for y in range(x+1):
            print("*",end=" ")
        print()

print()

def number(a):
    i=1
    while i<=a:
        j=1
        while j<=i:
            print("$",end=" ")
            j+=1
        i+=1
        print()

print()
def aplha(a):
    for x in range(a):
        for y in range(a):
            print("A",end=" ")
        print()
