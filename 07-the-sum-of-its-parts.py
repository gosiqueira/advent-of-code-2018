"""
Day 07 - The Sum of Its Parts
---
source: https://adventofcode.com/2018/day/7
"""

import argparse
import string
import time
from collections import deque

from utils import get_input


def the_sum_of_its_parts(verbose=False):
    instructions = get_input(day=7)

    tasks = {}
    for ch in string.ascii_uppercase:
        tasks[ch] = set()
    for inst in instructions:
        tasks[inst[36]].add(inst[5])

    schedule = ''
    while len(schedule) < 26:
        for t, dep in tasks.items():
            if t in schedule: continue

            if dep.issubset(set(schedule)):
                schedule += t
                break

    if verbose:
        print(f'The order the tasks should be: {schedule}')

    total_time = 0 
    workers = [{'remaining': 0, 'task': None} for _ in range(5)]
    queue = deque()
    done, doing = set(), set()

    while len(done) < 26:
        for k, v in tasks.items():
            if k in done or k in doing or k in queue:
                continue

            if v.issubset(done):
                queue.append(k)

        while queue:
            avail_worker = None
            for i in range(5):
                if workers[i]['task'] is None:
                    avail_worker = i
                    break

            if avail_worker is None:
                break

            task = queue.popleft()
            print(f'Task taken: {task}')
            workers[avail_worker]['task'] = task
            workers[avail_worker]['remaining'] = ord(task) - 4

        for i in range(5):
            if workers[i]['task']:
                workers[i]['remaining'] -= 1
                if workers[i]['remaining'] == 0:
                    task = workers[i]['task']
                    done.add(task)
                    doing.remove(task)
                    workers[i]['task'] = None

        total_time += 1
        print(total_time, workers)

    if verbose:
        print(f'Time taken to complete all the steps: {total_time}')

    return schedule, total_time


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2018 -- Day 07')
    parser.add_argument('--verbose', dest='verbose', action='store_true')
    args = parser.parse_args()
    
    tic = time.time()
    response = the_sum_of_its_parts(args.verbose)
    tac = time.time()
    print(*response)
    print(f'{tac - tic:.3f} s')
