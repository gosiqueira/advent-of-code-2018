"""
Day 01 - Chronal Calibration
---
source: https://adventofcode.com/2018/day/1
"""

import argparse
import time

from utils import get_input


def chronal_calibration(verbose=False):
    freqs = set()
    cur_freq, idx = 0, 0
    readings = get_input(day=1)

    total_freq = sum(readings)

    if verbose:
        print(f'Total freq: {total_freq}')

    while True:
        cur_freq += readings[idx % len(readings)]

        if cur_freq not in freqs:
           freqs.add(cur_freq)
        else:
            break

        idx += 1
    if verbose:
        print(f'First repeated freq: {cur_freq}')

    return total_freq, cur_freq


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2018 -- Day 01')
    parser.add_argument('--verbose', dest='verbose', action='store_true')
    args = parser.parse_args()
    
    tic = time.time()
    response = chronal_calibration(args.verbose)
    tac = time.time()
    print(*response)
    print(f'{tac - tic:.3f} s')