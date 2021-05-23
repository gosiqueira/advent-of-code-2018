"""
Day 06 - Chronal Coordinates
---
source: https://adventofcode.com/2018/day/6
"""

import argparse
import time

from utils import get_input, manhatan_dist


def chronal_coordinates(verbose=False):
    raw_coordinates = get_input(day=6)
    coords = {}

    grid_x, grid_y = 0, 0
    for coord in raw_coordinates:
        x, y = [int(c) for c in coord.split(',')]
        if grid_x < x: grid_x = x
        if grid_y < y: grid_y = y
        coords[(x, y)] = 0

    grid_x += 1
    grid_y += 1

    distances = [[[manhatan_dist((i, j), c) for c in coords.keys()] for j in range(grid_y)] for i in range(grid_x)]
    infinities = {}
    keys = list(coords.keys())

    for i in range(grid_x):
        for j in range(grid_y):
            min_dist = min(distances[i][j])
            
            if distances[i][j].count(min_dist) <= 1:
                key = keys[distances[i][j].index(min_dist)]
                coords[key] += 1
                if i == 0 or i == grid_x - 1 or j == 0 or j == grid_y - 1:
                    infinities[key] = 0

    for key in infinities.keys():
        coords[key] = 0               

    max_area = coords[max(coords, key=coords.get)]

    if verbose:
        print(f'Largest area size: {max_area}')

    valid_regions = 0
    for i in range(grid_x):
        for j in range(grid_y):
            if sum(distances[i][j]) < 10000:
                valid_regions += 1

    if verbose:
        print(f'Number of valid regions less than 10000 distance from all coordinates: {valid_regions}')

    return max_area, valid_regions


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2018 -- Day 06')
    parser.add_argument('--verbose', dest='verbose', action='store_true')
    args = parser.parse_args()
    
    tic = time.time()
    response = chronal_coordinates(args.verbose)
    tac = time.time()
    print(*response)
    print(f'{tac - tic:.3f} s')