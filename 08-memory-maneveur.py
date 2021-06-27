"""
Day 08 - Memory Maneuver
---
source: https://adventofcode.com/2018/day/8
"""

import argparse
import time

from utils import get_input


class TreeNode:
    def __init__(self, children=[], metadata=[], value=0):
        self.children = children
        self.metadata = metadata
        self.value = value


def gen_tree(data):
    n_children = data[0]
    n_meta     = data[1]

    data = data[2:]
    
    children = []
    for child in range(n_children):
        child, data = gen_tree(data)
        children.append(child)

    metadata = []
    for i in range(n_meta):
        metadata.append(data[i])

    value = 0
    if n_children == 0:
        value = sum(metadata)
    else:
        for metavalue in metadata:
            if metavalue - 1 < n_children:
                value += children[metavalue - 1].value

    root = TreeNode(children, metadata, value)

    return root, data[n_meta:]


def memory_maneuver(verbose=False):
    license_raw = get_input(day=8)
    license_numbers = list(map(int, license_raw[0].split()))

    root, _ = gen_tree(license_numbers)

    stack = [root]
    visited = set()
    metadata = []
    while stack:
        cur = stack.pop()

        metadata.extend(cur.metadata)
        visited.add(cur)

        for child in cur.children:
            if child not in visited: stack.append(child)

    meta_sum = sum(metadata)
    if verbose:
        print(f'The sum of the metadata is {meta_sum}')

    value = root.value
    if verbose:
        print(f'The value of the node A is {value}')

    return meta_sum, value


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2018 -- Day 08')
    parser.add_argument('--verbose', dest='verbose', action='store_true')
    args = parser.parse_args()
    
    tic = time.time()
    response = memory_maneuver(args.verbose)
    tac = time.time()
    print(*response)
    print(f'{tac - tic:.3f} s')