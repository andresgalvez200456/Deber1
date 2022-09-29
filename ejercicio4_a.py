from timeit import timeit
import json
import time

inicio = time .perf_counter()



def sum1(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sum2(n): 
    total = n*(n+1)//2
    return total

print(sum1(5), " ", sum2(5))

print( sum1(8), " ", sum2(8))

print( sum1(103), " ", sum2(103))

print( sum1(527), " ", sum2(527))


