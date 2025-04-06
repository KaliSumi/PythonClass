# Dicitionary 
# Stu={'Name':'Sumitha','Age':25,'City':'KKDI','DOB':'21-11-97'}
# print(Stu )

# print(Stu['Name'])
# print(Stu['Age'])
# print(Stu['City'])

# for x in Stu.keys():
#     print(x)

# for x in Stu.values():
#     print(x)
    
# for x in Stu:
#     print(f'{x}-{Stu[x]}')
    
# for x in Stu.items():
#     print(x)

# stu={}
# for x in range(3):
#     stu[x]=input("Enter the Values:")

# print(stu)

# stu={}
# for x in range(4):
#     stu[input("Enter the Keys:")]=input("Enter the Values:")
# print(stu)

#Nested dicitionay

# Stu={
#     0:{0:'Muthu',1:24,2:'KKDI'},
#     1:{0:'Ramu',1:25,2:'MDU'}
#     }
# print(Stu)

# for x in Stu:
#     for y in Stu[x]:
#         #print(f'[{x,y}]',end=" ")
#         print(Stu[x][y],end=" ")
#     print()
    
    
# stu={}
# temp={}
# for x in range(3):
#     for y in range(3):
#         temp[y]=input(f"Enter the Values [{x,y}]:")
#     stu[x]=temp
#     temp={}
# for x in stu:
#     for y in stu[x]:
#         print(stu[x][y],end=" ")
#     print()   


# a=[1,4,3,2,1,4,3,4]
# b=[1,2,4,3,5,4]
# a.extend(b)
# a=set(a)
# a=list(a)
# print(a)
res=[]
a=[1,4,3,2,1,4,3,4]
for x in a:
    if x not in res:
        res.append(x)
print(res)