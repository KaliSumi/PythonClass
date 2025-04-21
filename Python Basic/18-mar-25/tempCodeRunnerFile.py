a=65

while a<=69:
    b=65
    while b<=69:
        if a==b or a+b==134:
            print(chr(a),end=" ")
         
        else:
            print(" ",end=" ")
    
        b+=1
    print()
    a+=1