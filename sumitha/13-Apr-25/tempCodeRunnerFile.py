def square(i):
    print(i**2,end=" ")

num=[1,2,3,4,5,6,7,8,9,10]

print(*map(square,num))