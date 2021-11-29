#!/usr/bin/env python3

import random as r

rand_list = [ r.randrange(50) for x in range(10) ]


def partition(list, p, r):
    q, j = p, p

    while j < r:
        if list[j] > list[r]:
            j += 1
        else:
            list[j], list[q] = list[q], list[j]
            j += 1
            q += 1
    list[r], list[q] = list[q], list[r]
    return q

# print(partition([12, 7, 14, 9, 10, 11], 0, 5))



def quick_sort(list, p, r):
    if len(list[p:r+1]) < 2:
        return list

    q = partition(list, p, r)
    quick_sort(list, p, q-1)
    quick_sort(list, q+1, r)
    return list

print(quick_sort(rand_list, 0, len(rand_list)-1))
rand_list.sort()
print(rand_list)
