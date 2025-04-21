# from string import *
# for x in ascii_letters:
#     print(x,end=" ")
# print()
# for x in ascii_lowercase:
#     print(x,end=" ")
# print()
# for x in ascii_uppercase:
#     print(x,end=" ")
# print()
# x="123"
# print(x.isupper())
# print(x.islower())
# print(x.isalpha())
# print(x.isalnum())
# print(x.isdigit())
# print(x.isdecimal())
# print(x.isnumeric())
# l='muthuKumar'
# print(l.upper())
# print(l.lower())
# print(l.capitalize())
#print("Tom"*3)

# from datetime import *
# print(datetime.now())
# print(datetime.now().date())
# print(datetime.now().date().day)
# print(datetime.now().date().month)
# print(datetime.now().date().year)
# print(datetime.now().time())
# print(datetime.now().time().hour)
# print(datetime.now().time().minute)
# print(datetime.now().time().second)

#type 1 No Parameter & No Return Type 
#function declare
# def Rev():
#     inp=input("Enter the Name:")
#     print(inp[::-1])

# #function Calling 
# # Rev()
# # print("Hello")
# # Rev()
# # print("Jack")
# # Rev()
# for x in range(5):
#     Rev()


#type 2 With Parameter & No Return Type 
# def rev(para1):#parameter 
#     print(para1[::-1])


# names=[]
# for x in range(5):
#     names.append(input(f"Enter Name {x+1}:"))

# for x in names:
#     rev(x)#Function calling x is argument 



#type 3 with parameter & with return type 

# def rev(para1):
#     return para1[::-1]

# names=[]
# for x in range(3):
#     names.append(input(f"Enter Name {x+1}:"))

# for x in names:
#     print(rev(x))#Function calling x is argument 


# def add(a,b):
#     # return a+b
#     return checker(a+b)

# def checker(res):
#     print("Odd") if res%2!=0 else print("Even")


# checker(add(10,21))
# r=add(1,3)
# checker(r)

# add(10,34)

# #type 4-No parameter with return type:
# def rev():
#     inp=input("Enter the Name:")
#     return inp[::-1]
# print(rev())


# def AlphaCase():
#     inp=input("Enter the Name:")
#     if inp.islower():
#         print(inp.upper())
#     else:
#         print(inp.lower())

# AlphaCase()

# def AlphaCase(para):
#     if para.islower():
#         print(para.upper())
#     else:
#         print(para.lower())

# inp=input("Enter the Name:")
# AlphaCase(inp)

# from math import *
# def square(n):
#     res=[]
#     for x in n:
#         res.append(int(pow(x,2)))
#     return res


# num=[]
# for x in range(1,11,1):
#     num.append(x)

# print(square(num))



# x=10
# y='p'
# def show():
#     global x,y
#     x=100
#     y='a'
#     print(x)
#     print(y)


# print(x,y)
# show()
# print(x,y)


#function calling 
#call by Value - we pass the copy of data as a parameter to function.So , the value change inside the function 
#will not reflect outside the function 

# def show(x):
#     x+=100
#     print("value of x inside the function ",x)

# x=100
# show(x)
# print("value of x outside the function is ",x)

#call by reference - we pass the address of the variable as a parameter to the function .so , the value change inside the 
#function will be reflected outside the function 

# num=[1,2,3,4,5]
# def s(n):
#     n.append(100)
#     print(n)
# s(num)
# print(num)

#recursive function - function call by itself

def fact(i):
    if i==1:
        return 1
    else:
        return i+fact(i-1)    
print(fact(5))

'''
5==1    return 5*fact(4)=24*5=120
4==1    return 4*fact(3)=4*6=24
3==1    return 3*fact(2)=3*2=6
2==1    return 2*fact(1)=2*1=2
1==1    return 1

'''
