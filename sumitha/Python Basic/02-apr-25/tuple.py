# mark=(10,20,30,10,20,50)
# mark=list(mark)
# mark[0]=100
# print(mark)
# mark=tuple(mark)
# print(mark)
# # mark[0]=100
# for x in mark:
#     print(x)
# print(mark.count(20))
# print(len(mark))

# color=('red','green','blue')
# #unpack
# # apple,lemon,berry=color
# a,*b=color
# # print(apple,lemon,berry)
# print(a,b)

mark={'a','a','b','c'}
mark=list(mark)
mark[0]='e'
mark=set(mark)
print(mark)
for x in mark:
    print(x)