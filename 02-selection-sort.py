#!/usr/bin/env python3

import random as r

rand_list = [ r.randrange(50) for x in range(10) ]


def is_index_valid(list, index):
    return index >= 0 and index <= len(list) - 1

def swap(list, first, second):
    if not is_index_valid(list, first):
        print('First index invalid')
        return list
    if not is_index_valid(list, second):
        print('Second index invalid')
        return list

    list[first], list[second] = list[second], list[first]

    return list

# print(swap([1,2,3], 0, 2))
# print([3,2,1])
# print(swap([1,2,3], -1, 2))
# print(swap([1,2,3], 5, 2))
# print(swap([1,2,3], 1, -1))
# print(swap([1,2,3], 1, 5))

def get_min(list, startIndex):
    min = list[startIndex]
    minIndex = startIndex

    for i, val in enumerate(list[startIndex+1:], start=startIndex+1):
        if val < min:
            min = val
            minIndex = i

    return minIndex

# print(get_min([3, 2, 1], 0), 2)



def selection_sort(list):
    new_list = [ *list ]
    for i, val in enumerate(new_list):
        swap(new_list, i, get_min(new_list, i))

    return new_list

print(rand_list)
print(selection_sort(rand_list))
rand_list.sort()
print(rand_list)
