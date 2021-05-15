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
    for elf_id, start, size in zip(raw_claims[::4], raw_claims[2::4], raw_claims[3::4]):
        elf_id = int(elf_id[1:])
        x, y = map(int, start[:-1].split(','))
        h, w = map(int, size.split('x'))
        claims.append([elf_id, x, y, h, w])

    fabric = {}

    for _, x, y, h, w in claims:
        for dx in range(h):
            for dy in range(w):
                pos = (x+dx, y+dy)
                fabric[pos] = fabric.get(pos, 0) + 1

    overlaps = sum([val > 1 for val in fabric.values()])

    if verbose:
        print(f'Square inches of fabric within two or more claims: {overlaps}')

    unique_id = 0

    for elf_id, x, y, h, w in claims:
        unique = True
        for dx in range(h):
            for dy in range(w):
                pos = (x+dx, y+dy)
                if fabric[pos] > 1:
                    unique = False

        if unique == True:
            unique_id = elf_id

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