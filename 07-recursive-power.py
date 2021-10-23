#!/usr/bin/env python3

import random as r

def recursive_power(base, power):
    if power == 0:
        return 1
    if power < 0:
        return 1 / recursive_power(base, -power)
    if power % 2 == 1:
        return base * recursive_power(base, power-1)
    if power % 2 == 0:
        return recursive_power(base, power/2) * recursive_power(base, power/2)

print('###')
print(recursive_power(2, 0), 1)
print(recursive_power(2, 1), 2)
print(recursive_power(2, 4), 16)
print(recursive_power(2, 5), 32)
print(recursive_power(3, 3), 27)
print(recursive_power(3, -3), 0.037037037037037035)
