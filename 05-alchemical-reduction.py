"""
Day 05 - Alchemical Reduction
---
source: https://adventofcode.com/2018/day/5
"""

import argparse
import time

from collections import deque
from utils import get_input


def react(polymer):
    stack = []
    for ch in polymer:
        if len(stack) == 0 or abs(ord(ch) - ord(stack[-1])) != 32:
            stack.append(ch)
        else:
            stack.pop()

    return len(stack)

def alchemical_reduction(verbose=False):
    polymer = list(get_input(day=5)[0])
    

    remaining_units = react(polymer)

    if verbose:
        print(f'Remaining polimer units: {remaining_units}')

    min_polymer_len = len(polymer)
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVXWYZ':
        modified_polymer = ''.join([unit for unit in polymer if unit.upper() != ch])
        polymer_len = react(modified_polymer)
        if polymer_len < min_polymer_len:
            min_polymer_len = polymer_len

    if verbose:
        print(f'Minimum polymer length: {min_polymer_len}')

    return remaining_units, min_polymer_len


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2018 -- Day 05')
    parser.add_argument('--verbose', dest='verbose', action='store_true')
    args = parser.parse_args()
    
    tic = time.time()
    response = alchemical_reduction(args.verbose)
    tac = time.time()
    print(*response)
    print(f'{tac - tic:.3f} s')