"""
Day 03 - No Matter How You Slice It
---
source:
source: https://adventofcode.com/2018/day/3
"""

import argparse
import time

from utils import get_input


def no_matter_how_you_slice_it(verbose=False):
    raw_claims = get_input(day=3)

    claims = []
    for claim in raw_claims:
        elf_id, _, start, size = claim.split()
        elf_id = int(elf_id[1:])
        x, y = map(int, start[:-1].split(','))
        w, h = map(int, size.split('x'))
        claims.append([elf_id, x, y, w, h])

    fabric = {}

    for _, x, y, w, h in claims:
        for dx in range(w):
            for dy in range(h):
                pos = (x+dx, y+dy)
                fabric[pos] = fabric.get(pos, 0) + 1

    overlaps = sum([val > 1 for val in fabric.values()])

    if verbose:
        print(f'Square inches of fabric within two or more claims: {overlaps}')

    unique_id = 0

    for elf_id, x, y, w, h in claims:
        unique = True
        for dx in range(w):
            for dy in range(h):
                pos = (x+dx, y+dy)
                if fabric[pos] > 1:
                    unique = False
                    break

        if unique == True:
            unique_id = elf_id
            break

    if verbose:
        print(f'Elf ID without overlaps: {unique_id}')

    return overlaps, unique_id


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2018 -- Day 03')
    parser.add_argument('--verbose', dest='verbose', action='store_true')
    args = parser.parse_args()
    
    tic = time.time()
    response = no_matter_how_you_slice_it(args.verbose)
    tac = time.time()
    print(*response)
    print(f'{tac - tic:.3f} s')