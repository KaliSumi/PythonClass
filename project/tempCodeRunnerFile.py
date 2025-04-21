from math import*
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
op=int(input("1.add\n2.sub\n3.mult\n4.div\n5.floor div\n6.square\n7.power"))
if op==1:
    print("add",a+b)
elif op==2:
    print("sub",a-b)
elif op==3:
    print("mult",a*b)
elif op==4:
    print("div",a/b)
elif op==5:
    print("floordiv",(a//b))
elif op==6:
    print("squar",sqrt(a),sqrt(b))
elif op==7:
    print("power",pow(a,b))