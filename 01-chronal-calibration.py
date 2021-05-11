"""
Day 01 - Chronal Calibration
---
source: https://adventofcode.com/2018/day/1
"""

from utils import get_input


def chronal_calibration():
    freqs = set()
    cur_freq, idx = 0, 0
    readings = get_input(day=1)

    print(f'Total freq: {sum(readings)}')

    while True:
        cur_freq += readings[idx % len(readings)]

        if cur_freq not in freqs:
           freqs.add(cur_freq)
        else:
            break

        idx += 1

    print(f'First repeated freq: {cur_freq}')


if __name__ == '__main__':
    chronal_calibration()