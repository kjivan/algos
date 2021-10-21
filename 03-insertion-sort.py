#!/usr/bin/env python3

import random as r

rand_list = [ r.randrange(50) for x in range(10) ]


def insert(array, sort_index, index):
    if sort_index < 0 or sort_index > len(array) or index < 0 or index > len(array):
        print('invalid index')
        return array

    ins_val = array[index]
    array.pop(index)
    for i in range(sort_index, -1, -1):
        if ins_val > array[i]:
            array.insert(i+1, ins_val)
            return array

    array.insert(0, ins_val)
    return array

# print(insert([1,5,7, 2], 2, 3))
# print(insert([1,5,7, 0], 2, 3))
# print(insert([1,5,7, 9], 2, 3))

def insertion_sort(list):
    new_list = [ *list ]
    for i in range(1, len(list)):
        insert(new_list, i-1, i)

    return new_list

print(insertion_sort(rand_list))
rand_list.sort()
print(rand_list)
