from functools import reduce
fa=[1,2,3,4,5,6]
result=reduce(lambda x,y:x*y,fa,2)
print(result)