#!/usr/bin/env python3

import random as r

rand_list = [ r.randrange(50) for x in range(10) ]

def merge(a, b):
    c = []

    a_idx, b_idx, c_idx = 0, 0, 0;

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.insert(len(c), a[a_idx])
            a_idx += 1
        else:
            c.insert(len(c), b[b_idx])
            b_idx += 1

    while a_idx < len(a):
        c.insert(len(c), a[a_idx])
        a_idx += 1

    while b_idx < len(b):
        c.insert(len(c), b[b_idx])
        b_idx += 1
    return c



# print(merge([1,4,8], [2,3,8]), [1,2,3,4,8,8])
# print(merge([1,4], [2,3,8]), [1,2,3,4,8])
# print(merge([1,2,3], [1,2,3]), [1,1,2,2,3,3])

def merge_sort(list):
    if len(list) < 2:
        return list

    a = merge_sort(list[0:int(len(list)/2)])
    b = merge_sort(list[int(len(list)/2):])
    return merge(a,b)

    return new_list

print(merge_sort(rand_list))
rand_list.sort()
print(rand_list)
