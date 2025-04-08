# inp=input("Enter the Word:")
# st=''
# for x in inp:
#     if x=='0':
#         st=st+'1'
#     elif x=='1':
#         st=st+'0'
#     else:
#         st=st+'-'

# print(st)

# inp=input("Enter the Word")
# if inp.lower()==inp[::-1].lower():
#     print("Pali")
# else:
#     print("Not a Pali")

# inp=input("Enter the word:")
# res=''
# for x in range(len(inp)-1,-1,-1):
#     res=res+inp[x].lower()
# print("Pali" if inp.lower()==res  else "Not a Pali")


# name="Muthu is a good guy"
# l=name.replace('Muthu','Lion')
# print(l)

# king = '001'
# res = king.replace('0', '2').replace('1', '0').replace('2', '1')
# print(res)

#named parameter

# def Show(name,age):
#     print("My Name is ",name,"\nMy age is ",age)
#     print(f'My Name is {name}\n My age is {age}')

# Show('Muthu',45)
# Show(age=45,name='Muthu')
    
# #optional parameter 
# def view(a=None):
#     print(a)

# view(12)
# view()

#Arbitrary Arguments, *args

# def show(*l):
#     print(list(l))

# show(1,2,3,4,5,6)

# #keyword Arguments 

# def show(**l):
#     print(l)
# show(name="Muthu",age=10)

#module is collection function 
from patterns import *
star(5)
number(5)
aplha(10)

#package is a collection of module
from sound.newsong import *
from sound.oldsong import *

new1()
new2()
new3()
new4()

old1()
old2()
old3()
old4()