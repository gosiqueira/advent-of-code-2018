"""
Day 04 - Repose Record
---
source: https://adventofcode.com/2018/day/4
"""

import argparse
import datetime
import time

from utils import get_input


def repose_record(verbose=False):
    records = sorted(get_input(day=4))

    guards = {}
    guard_id = 0
    start, end = 0, 0

    for record in records:
        date, activity = record.split(']')
        date, activity =  date[1:], activity.strip()

        if 'begins shift' in activity:
            guard_id = int(activity.split()[1][1:])
        elif 'falls asleep' in activity:
            start = int(date[-2:])
        elif 'wakes up' in activity:
            end = int(date[-2:])

            if guard_id not in guards: guards[guard_id] = [0] * 60

            for minute in range(start, end):
                guards[guard_id][minute] += 1
        else:
            print('ERROR')
            exit(1)


    sleeping_hours = {k: sum(v) for k, v in guards.items()}

    most_asleep_guard = max(sleeping_hours, key=sleeping_hours.get)
    minute_max = max(range(len(guards[most_asleep_guard])), key=guards[most_asleep_guard].__getitem__)
    most_asleep_key = most_asleep_guard * minute_max

    if verbose:
        print(f'Hash #1 ({most_asleep_guard} * {minute_max}): {most_asleep_key}')

    most_common_guard, minute_asleep, max_asleep_time = None, None, None
    for guard_id, minutes in guards.items():
        for minute, time_slept in enumerate(minutes):
            if not max_asleep_time or time_slept > max_asleep_time:
                most_common_guard = guard_id
                minute_asleep = minute
                max_asleep_time = time_slept

    most_common_key = most_common_guard * minute_asleep

    if verbose:
        print(f'Hash #2 ({most_common_guard} * {minute_asleep}): {most_common_key}')

    return most_asleep_key, most_common_key
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2018 -- Day 04')
    parser.add_argument('--verbose', dest='verbose', action='store_true')
    args = parser.parse_args()
    
    tic = time.time()
    response = repose_record(args.verbose)
    tac = time.time()
    print(*response)
    print(f'{tac - tic:.3f} s')