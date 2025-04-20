# from math import *
import math
def Armstrong(para):
    r=str(para)
    l=len(r)
    f=0
    for x in r:
        f=f+int(pow(int(x),l))
    print("Armstrong Number" if para == f  else "not a Armstrong number")
Armstrong(150)