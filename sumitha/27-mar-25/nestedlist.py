#nested list
mat=[[1,2,3],[4,5,6],[7,8,9]]
'''
mat[0]=[1,2,3]
mat[1]=[4,5,6]
mat[2]=[7,8,9]

mat[0][0]=1 mat[0][1]=2 mat[0][2]=3
mat[1][0]=4 mat[1][1]=5 mat[1][2]=6
mat[2][0]=7 mat[2][1]=8 mat[2][2]=9
'''

# print(mat)

# for row in range(0,len(mat),1):
#     for col in range(0,len(mat),1):
#         print(mat[row][col],end=" ")
#     print()

# for x in mat:
#     for y in x:
#         print(y,end=" ")
#     print()

# matA=[]
# temp=[]
# row=int(input("Enter the Number of Rows:"))
# col=int(input("Enter the Number of Cols:"))

# for x in range(row):
#     for y in range(col):
#         temp.append(input(f"Enter the lette[{x},{y}]:"))
#     matA.append(temp)
#     temp=[]

# for x in matA:
#     for y in x:
#         print(y,end=" ")
#     print()

matA=[]
matB=[]
temp=[]
c=0
row=int(input("enter the num of row:"))
col=int(input("enter the num of col:"))

for x in range(row):
    for y in range(col):
        temp.append(input(f"enter the letter[{x},{y}]:"))
    matA.append(temp)
    temp=[]
for x in range(row):
    for y in range(col):
        temp.append(input(f"enter the letter[{x},{y}]:"))
    matB.append(temp)
    temp=[]

for x in range(row):
    for y in range(col):
        if matA[x][y]==matB[x][y]:
            c=c+1
print("matA and matB is equal" if c==row*col else "matA and matB is not equal")
      

matA=[]
temp=[]
row=int(input("enter the num of row:"))
col=int(input("enter the num of col:"))
for x in range(row):
    for y in range(col):
        temp.append(int(input(f"enter the num[{x},{y}]:")))
    matA.append(temp)
    temp=[]
for x in matA:
    for y in x:
        print(y*2,end=" ")
    print() 

# mat1=[]
# temp=[]
# c=0
# row=int(input("enter the num of row:"))
# col=int(input("enter the num of col:"))
# for x in range(row):
#     for y in range(col):
#         temp.append(int(input(f"enter the num[{x},{y}]:")))
#     mat1.append(temp)
#     temp=[]

# for x in range(0,row,1):
#     for y in range(0,col,1):
#         if x==y and mat1[x][y]==1 or x!=y and mat1[x][y]==0:
#             c=c+1
# print("Is Identical Matrix") if c==row*col else print("Not a Identitcal Matrix")


