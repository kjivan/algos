#!/usr/bin/env python3

import random as r

def recursive_palindrome(string):
    if len(string) == 1 or len(string) == 0:
        return True
    return string[0] == string[-1] and recursive_palindrome(string[1:-1])

print('###')
print(recursive_palindrome(''), True)
print(recursive_palindrome('a'), True)
print(recursive_palindrome('cac'), True)
print(recursive_palindrome('cat'), False)
print(recursive_palindrome('xyxyx'), True)
print(recursive_palindrome('zxyzxy'), False)
