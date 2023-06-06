#!/usr/bin/env python3

import sys
import pyperclip
from pathlib import Path
from more_itertools import chunked


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
    total_sum = 0
    for line in data:
        a, b = line[:len(line)//2], line[len(line)//2:]
        both = set(a) & set(b)
        the_same = both.pop()
        if the_same.isupper():
            ascii_code = ord(the_same) - 38
        else:
            ascii_code = ord(the_same) - 96
        total_sum += ascii_code
    return total_sum


def part_2(data):
    total_sum = 0
    a, b, c = "", "", ""
    for group in chunked(data, 3):
        a, b, c = group
        both = set(a) & set(b) & set(c)
        the_same = both.pop()
        if the_same.isupper():
            ascii_code = ord(the_same) - 38
        else:
            ascii_code = ord(the_same) - 96
        total_sum += ascii_code
    return total_sum


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
