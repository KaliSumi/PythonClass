# email=input("enter the email:")
# print(email)

# num1=int(input("enter the whole number"))
# num2=float(input("enter the pointing number"))
# print(int(num1+num2))

# birth_year=int(input("enter the birthyear"))
# current_year=int(input("enter the current year"))
# print("age:",current_year-birth_year)

# name=input("enter the name:")
# year=int(input("enter the year:"))
# if year%2==0:
#     print(name+str(year%100)+"@gmail.com")
# else:
#     print(name+str(year%100)+"@yahoo.com")

# num1=int(input("enter the num1:"))
# num2=int(input("enter the num2:"))
# num3=float(input("enter the num3:"))
# r=int(num1+num2+num3)//10
# print(r)
# if r%2==0:
#     print("even")
# else:
#     print("odd")



# name=input("enter the name")
# if name>='0' and name<='9':
#     print('number')
# elif name>='a' and name<='z' or name>='A' and name<='Z':
#     print('alpha')
# else:
#     print('special char')

name=input("enter the role:")
if name=='staff':
    print("red and green")
elif name=='student':
    print("blue and black")
else:
    print("orange")

g='no grade'
mark=int(input("enter the mark:"))
if mark>=35:
    if mark>90 and mark<=100:
        g="a"
    elif mark>=80 and mark<=90:
        g="b"
    elif mark>=70 and mark<=79:
        g="c"
    elif mark>=60 and mark<=69:
        g="d"
    elif mark>=50 and mark<=59:
        g="e"
    print(g,'-Pass')
else:
    print(g,"-fail")

a=int(input("enter the num:"))
if a%3==0 and a%5==0:
    r=a*2
elif a%3==0:
    r=a*3
elif a%5==0:
    r=a*4
print(r)

name=input("enter the name:")
print(name,"is my student")

name=input("enter the name:")
if  name>='a' and name<='z' or name>='A' and name<='Z':
    print('its a alpha')
elif name>='0' and name<='9':
    print('its a numaric')
else:
    print('its a aplhanumeric')

name=input("enter the name:")
if name>='0' and name<='9':
    print('its a numaric')
elif name>='a' and name<='z' or name>='A' and name<='Z':
    print('its a albha')
else:
    print('its a albha numaric')


a=int(input("enter the number"))
b=int(input("enter the number"))
r= int(input("1.Add\n2.Sub\n3.Mul:"))
if r==1:
    print(a+b)
elif r==2:
    print(a-b)


a=int(input('enter a:'))
b=int(input('enter b:'))
print('add'if a+b>0 else 'sub')



age=int(input("enter the number"))
if age>=0:
    print('positive')
    if age>=0 and age<=9:
        print('kid')
    elif age>=10 and age<=17:
        print('teen')
    elif age>=18 and age<=25:
        print('youngster')
    elif age>=26 and age<50:
        print('citizen')
    else:
        print('seniour citizen')
else:
    print('not valied')

    