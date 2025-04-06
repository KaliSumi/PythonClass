# i=1
# while True:
#     print(i)
#     i+=1
#     if i>10:
#         break

# print("Thank You")

# for x in range(1,11,1):
#     if  x==3 or x==5 :
#         continue
#     print(x)    

# print("Thank you")


# for x in range(1,11,1):
#     if x%2==0:
#         pass
#     print(x)    
# print("Thank you")


#list 
# mark=[15,25,45,78,85]
# print(mark)
# mark[2]=100
# print(mark[2])
#mark[0]=15
#mark[1]=25
#mark[2]=45
#mark[3]=78
#mark[4]=85


mark=[15,25,45,78,85]
# i=0
# while i<5:
#     print(mark[i]+15)
#     i+=1

# for x in range(0,5,1):
#     print(mark[x]*2)

# for x in mark:
#     print(x*2,end=" ")

# for x in range(0,5,1):
#     print(x,'=',mark[x])




# mark=[]#empty list 
# no=int(input("Enter the No Subject:"))

# #to get values from the user and store it in a list 
# for x in range(0,no,1):
#     mark.append(int(input(f"Enter the Marks {x+1}:")))
    
# #to display the result from list 
# for x in mark:
#     print(x)



# mark=[]#empty list 
# no=int(input("Enter the No Subject:"))

# #to get values from the user and store it in a list 
# for x in range(0,no,1):
#         while True:
#             m=int(input(f"Enter the Marks {x+1}:"))
#             if m>0 and m<=100:
#                 mark.append(m)
#                 break
#             else:
#                 print("In Valid Mark")  
# #to display the result from list 
# for x in mark:
#     print(x)

# a=[1,2,3]
# b=[4,5,6]
# c=['a','b','c']
# a.extend(b)
# a.extend(c)
# print(a)

# a=[1,2,3]
# b=['a','b','c']
# a.insert(2,b)
# a.insert(0,'Apple')
# print(a)

# a=[1,2,3,4,5,6,3,4,5,6]
# for x in a:
#     if x==3 or x==6:
#         a.remove(x)
# print(a)


# a=[1,2,3,4,5,6]
# a.pop()
# print(a)


# a=[1,2,3,4,5,6]
# a.pop(2)
# print(a)

# a=[1,2,3,4,5]
# a.clear()
# print(a)

# a=[1,2,3,4,5]
# del(a)
# print(a)

# fruits=['apple','orange','Lemon','Green Apple']
# name=input("Enter the Fruits:")
# if name in fruits:
#     print(fruits.index(name))
# else:
#     print("No Fruits Aviable")
# # print(fruits.index('apple'))
# # print(fruits.index('Lemon'))
# # if 'Green' in fruits:
# #     print(fruits.index('Green'))


# l=[1,2,3,4,5,6,1,2,3,4,1,5,6,1,90]
# print(len(l))
# print(l.count(1))
# l=['a','e','c','d','b']
# # l.sort()
# l.sort(reverse=True)
# print(l)

# l=['a','e','c','d','b']
# l.sort()
# l.reverse()
# print(l)
# l=['a','e','c','d','b']
# k=l.copy()
# print(l,k)

# name=input("Enter the Name:")
# print(name)
# print(list(name))

name=input("Enter the Name:").split("-")
print(name)

words = ["Hello", "world", "from", "Python"]
sentence="".join(words)
print(sentence)