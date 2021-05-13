"""
Day 02 - Inventory Management System
---
source: https://adventofcode.com/2018/day/2
"""

import argparse
import time

from collections import Counter

from utils import get_input


def inventory_management_system(verbose=False):
    ids = get_input(day=2)

    occurrences = dict()
    two_ocurrences = 0
    three_ocurrences = 0

    for id in ids:
        occurrences[id] = Counter(Counter(id).values())
        if 2 in occurrences[id]: two_ocurrences += 1
        if 3 in occurrences[id]: three_ocurrences += 1

    checksum = two_ocurrences * three_ocurrences

    if verbose:
        print(f'Checksum: {checksum}')

    same_chars = ''
    for idx1 in range(len(ids)):
        for idx2 in range(idx1, len(ids)):
            id1, id2 = ids[idx1], ids[idx2]
            if sum(ch1 != ch2 for ch1, ch2 in zip(id1, id2)) == 1:
                same_chars = ''.join([ch1 for ch1, ch2 in zip(id1, id2) if ch1 == ch2])
                print(f'Same characters between ids {id1} and {id2}: {same_chars}')

    return checksum, same_chars


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2018 -- Day 02')
    parser.add_argument('--verbose', dest='verbose', action='store_true')
    args = parser.parse_args()
    
    tic = time.time()
    response = inventory_management_system(args.verbose)
    tac = time.time()
    print(*response)
    print(f'{tac - tic:.3f} s')