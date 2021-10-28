#!/usr/bin/env python3

import random as r


# populate one peg with discs
def setup_tower(peg, num_discs):
    if peg < 0 or peg > 2:
        print('Peg out of range (3<peg < 0 peg < 3)')
        return
    # setup hanoi with 3 pegs
    hanoi = [[],[],[]]
    hanoi[peg] = [ x for x in range(1,num_discs+1) ]
    return hanoi

# print(setup_tower(-1,2), None)
# print(setup_tower(3,2), None)
# print(setup_tower(1,2),[[],[1,2],[]])
# print(setup_tower(0,3),[[1,2,3],[],[]])

def move_disc(tower, from_peg_index, to_peg_index):
    from_peg = tower[from_peg_index]
    to_peg = tower[to_peg_index]

    if len(to_peg) != 0 and to_peg[0] < from_peg[0]:
        print('Illegal move')
        return
    from_value = from_peg.pop(0)
    to_peg.insert(0,from_value)
    return tower

# print(move_disc([[1],[2, 3],[]], 1,2), [[1],[3],[2]])
# print(move_disc([[],[2, 3],[1]], 1,2), 'illegal move')

def solve_tower(tower, num_discs, from_peg, to_peg):
    if num_discs == 0:
        return tower
    solve_tower(tower, num_discs-1, from_peg, 3 - (from_peg + to_peg) )
    move_disc(tower, from_peg, to_peg)
    solve_tower(tower, num_discs-1, 3 - (from_peg + to_peg), to_peg )
    return tower

print(solve_tower(setup_tower(0, 1), 1, 0, 2), setup_tower(2, 1))
print(solve_tower(setup_tower(0, 2), 2, 0, 2), setup_tower(2, 2))
print(solve_tower(setup_tower(0, 4), 4, 0, 2), setup_tower(2, 2))
