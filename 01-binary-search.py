#!/usr/bin/env python3

list = [1, 3, 5, 8, 9, 10]

def search(list, target):
    min = 0
    max = len(list) - 1

    while True:
        if max < min:
            return -1

        guess_index = int((min + max) / 2)
        guess_val = list[guess_index]

        if (guess_val == target):
            return guess_index
        elif (target < guess_val):
            max = guess_index - 1
        else:
            min = guess_index + 1

print(search(list, 3), 1)
print(search(list, 9), 4)
print(search(list, 4), -1)
