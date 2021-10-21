#!/usr/bin/env python3

import random as r

def iterative_factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

print('###')
print(iterative_factorial(0), 1)
print(iterative_factorial(1), 1)
print(iterative_factorial(3), 6)
print(iterative_factorial(10), 3628800)
