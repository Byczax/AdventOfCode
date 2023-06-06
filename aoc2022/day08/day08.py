#!/usr/bin/env python3

import sys
import pyperclip
from pathlib import Path
from collections import defaultdict
import json
# import sys
# sys.setrecursionlimit(100000)


def read_file(filename: str) -> list:
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [i.strip() for i in lines]


def print_and_copy(text: str, result) -> None:
    print(f'{text} - {result}')
    pyperclip.copy(result)
    print(f'{text} Copied to clipboard')
    input('Press enter to continue...')


def main(filename):
    data = read_file(filename)

    print_and_copy('Part 1', part_1(data))
    print_and_copy('Part 2', part_2(data))


def part_1(data):
    counter = 0
    tree_map = []
    for line in data:
        tree_map.append([i for i in line])

    for i in range(len(tree_map)):
        for j in range(len(tree_map[i])):
            visible = True
            tree_size = tree_map[i][j]
            # visible from top
            k = i - 1
            while k >= 0:
                if tree_map[k][j] >= tree_size:
                    visible = False
                    break
                k -= 1
            if visible:
                counter += 1
                continue
            # visible from bottom
            visible = True
            k = i + 1
            while k < len(tree_map):
                if tree_map[k][j] >= tree_size:
                    visible = False
                    break
                k += 1
            if visible:
                counter += 1
                continue
            # visible from left
            visible = True
            k = j - 1
            while k >= 0:
                if tree_map[i][k] >= tree_size:
                    visible = False
                    break
                k -= 1
            if visible:
                counter += 1
                continue
            # visible from right
            visible = True
            k = j + 1
            while k < len(tree_map[i]):
                if tree_map[i][k] >= tree_size:
                    visible = False
                    break
                k += 1
            if visible:
                counter += 1
                continue
    # counter += len(tree_map)*2 + len(tree_map[0])*2 - 4

    return counter


def part_2(data):
    counter = [0, 0, 0, 0]
    tree_map = []
    best = 0
    visible = 0
    for line in data:
        tree_map.append([i for i in line])

    for i in range(1, len(tree_map) - 1):
        for j in range(1, len(tree_map[i]) - 1):
            tree_size = tree_map[i][j]
            # visible from top
            k = i - 1
            while k >= 0:
                counter[0] += 1
                if tree_map[k][j] >= tree_size:
                    break
                k -= 1

            # visible from left
            k = j - 1
            while k >= 0:
                counter[1] += 1
                if tree_map[i][k] >= tree_size:
                    break
                k -= 1
            # visible from right
            k = j + 1
            while k < len(tree_map[i]):
                counter[2] += 1
                if tree_map[i][k] >= tree_size:
                    break
                k += 1

            # visible from bottom
            k = i + 1
            while k < len(tree_map):
                counter[3] += 1
                if tree_map[k][j] >= tree_size:
                    break
                k += 1

            result = counter[0] * counter[1] * counter[2] * counter[3]
            if result > best:
                best = result
            counter = [0, 0, 0, 0]
    return best


if __name__ == "__main__":
    if len(sys.argv) < 2:
        if Path("input.txt").exists():
            filename = "input.txt"
        else:
            print("\033[1;31mHey, file 'input.txt' don't exist, " +
                  "try to give a path to file: \033[1;32m"
                  "python.exe " + sys.argv[0] + " <filename>"
                  "\033[1;m")
            sys.exit(1)
    else:
        filename = sys.argv[1]
    main(filename)
