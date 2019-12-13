#!/usr/bin/python

import sys


def recurse(prev, n, all_results):
    if n == 0:
        return prev

    with_rock = recurse(prev + ['rock'], n - 1, all_results)
    with_paper = recurse(prev + ['paper'], n - 1, all_results)
    with_scissors = recurse(prev + ['scissors'], n - 1, all_results)

    return [with_rock, with_paper, with_scissors]


def rock_paper_scissors(n):
    results = []
    recurse([], n, results)

    return results


rock_paper_scissors(1)
rock_paper_scissors(2)
rock_paper_scissors(3)
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
