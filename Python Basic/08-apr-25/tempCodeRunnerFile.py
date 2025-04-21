l=[]
def num():
    inp=int(input("enter the number:"))
    for x in range(1,11,1):
        l.append(f'{x}*{inp}={x*inp}')
    return l
for x in num():
     print(x)