#!/usr/bin/env python3

import sys
import pyperclip
from pathlib import Path
import numpy as np


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
    overlapped = 0
    for line in data:
        sec1, sec2 = line.split(",")
        sec1 = sec1.split("-")
        sec2 = sec2.split("-")
        if int(sec1[0]) <= int(sec2[0]) and int(sec1[1]) >= int(sec2[1]):
            overlapped = overlapped + 1
        elif int(sec1[0]) >= int(sec2[0]) and int(sec1[1]) <= int(sec2[1]):
            overlapped = overlapped + 1
    return overlapped


def part_2(data):
    overlapped = 0
    for line in data:
        sec1, sec2 = line.split(",")
        sec1 = [int(i) for i in sec1.split("-")]
        sec2 = [int(i) for i in sec2.split("-")]
        arr1 = np.linspace(
            sec1[0], sec1[1], (sec1[1]-sec1[0])*int(1)+1).tolist()
        arr2 = np.linspace(
            sec2[0], sec2[1], (sec2[1]-sec2[0])*int(1)+1).tolist()
        diff = set(arr1) & set(arr2)
        if diff:
            overlapped = overlapped + 1
    return overlapped


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
