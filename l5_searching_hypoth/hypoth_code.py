import time
import random

def linear(tab,targ):
    startTime = time.tick()
    for item in tab:
        if item == targ:
            return True,time.tick() - startTime
    return False,time.tick() - startTime

def binary(tab,targ):
    pass

def jump(tab,targ):
    pass

def sublist(tab,targ):
    pass

Table1 = [random.randint(1,100) for x in range(1,10000000)]
Table2 = [x for x in range(1,100)]
Table3 = [x for x in range(1,100)][::-1]

print(linear(Table1,50))
print(linear(Table2,50))
print(linear(Table3,50))
