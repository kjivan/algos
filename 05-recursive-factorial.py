#!/usr/bin/env python3

import random as r

def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)

print('###')
print(recursive_factorial(0), 1)
print(recursive_factorial(1), 1)
print(recursive_factorial(3), 6)
print(recursive_factorial(10), 3628800)
