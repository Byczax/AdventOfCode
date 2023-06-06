#!/usr/bin/env python3

import sys
import pyperclip
from pathlib import Path
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
    part_2_2(data)


def part_1(data):
    fields = set()
    fields.add((0, 0))
    head = [0, 0]
    tail = [0, 0]
    for command in data:
        direction, value = command.split(" ")
        if direction == 'R':
            for _ in range(int(value)):
                head[1] += 1
                if abs(head[1] - tail[1]) > 1:
                    tail[1] += 1
                    if head[0] != tail[0]:
                        tail[0] = head[0]
                    fields.add((tail[0], tail[1]))
                    # print(f'adding {tail}')
                # print(head, tail)
        elif direction == 'L':
            for _ in range(int(value)):
                head[1] -= 1
                if abs(head[1] - tail[1]) > 1:
                    tail[1] -= 1
                    if head[0] != tail[0]:
                        tail[0] = head[0]
                    fields.add((tail[0], tail[1]))
                # print(head, tail)
        elif direction == 'U':
            for _ in range(int(value)):
                head[0] += 1
                if abs(head[0] - tail[0]) > 1:
                    tail[0] += 1
                    if head[1] != tail[1]:
                        tail[1] = head[1]
                    fields.add((tail[0], tail[1]))
                # print(head, tail)
        elif direction == 'D':
            for _ in range(int(value)):
                head[0] -= 1
                if abs(head[0] - tail[0]) > 1:
                    tail[0] -= 1
                    if head[1] != tail[1]:
                        tail[1] = head[1]
                    fields.add((tail[0], tail[1]))
                # print(head, tail)
    # print(fields)
    return len(fields)


def part_2(data):
    fields = set()
    fields.add((0, 0))
    x, y = [0]*10, [0]*10
    for command in data:
        direction, value = command.split(" ")
        for _ in range(int(value)):
            x[0] += {"U": 0, "R": 1, "D": 0, "L": -1}[direction]
            y[0] += {"U": -1, "R": 0, "D": 1, "L": 0}[direction]
            for j in range(1, len(x)):
                while abs(x[j] - x[j-1]) > 1 or abs(y[j] - y[j-1]) > 1:
                    x[j] += (x[j-1] > x[j]) - (x[j-1] < x[j])
                    # if x[j-1] > x[j]:
                        # x[j] += 1
                    # if x[j-1] < x[j]:
                        # x[j] -= 1
                    y[j] += (y[j-1] > y[j]) - (y[j-1] < y[j])
                    # if y[j-1] > y[j]:
                        # y[j] += 1
                    # if y[j-1] < y[j]:
                        # y[j] -= 1
            fields.add((x[-1], y[-1]))
    return len(fields)


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
