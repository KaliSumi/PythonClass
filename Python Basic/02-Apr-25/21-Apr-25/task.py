# flower=[]
# def writedata():
#     global flower
#     f=open('flower.txt','w')
#     no=int(input("Enter the No.of.flowers Names:"))
#     for x in range(no):
#         f.write(input("Enter the flowersNames:")+'\n')
#     f.close()
# writedata()

# def readdata():
#     f=open("flower.txt",'r')
#     flower=f.read()
#     f.close

# def addflower():
#     f=open('flower.txt','a')
#     for x in range(3):
#         f.write(input("Enter the flowersNames:")+'\n')
#     f.close()
# writedata()
# readdata()
# addflower()

# # square Each Number in a List:
# def fun(i):
#     for x in i:
#         yield x**2
# list=[1,2,3,4,5,6,7,8,9,10]
# print(*fun(list))

# filter even numbers:
num=[1,2,3,4,5,6,7,8,9,10]
def evennumber(k):
    if k%2==0:
        return num
    print(*map(filter,num))

# positive number
num=[0,-1,-3,-5,3,9,8,10]
def positve(num):
    if num>=0:
        print(num)

# List Comprehension:
flower=['Lotus','Lily','Marogold','daisy','Lavender','Hibiscus']
print(x for x in flower if 'a' in 'x')

        