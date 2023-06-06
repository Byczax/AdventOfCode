#!/usr/bin/env python3

import sys
import pyperclip
from pathlib import Path


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

    print_and_copy('Part 1', part_1_2(data[0], 4))
    print_and_copy('Part 2', part_1_2(data[0], 14))


def part_1_2(data, data_length):
    full_counter = data_length
    letters = [i for i in data[0:data_length]]
    print(letters)
    for letter in data[data_length:]:
        test_set = set(letters)
        if len(test_set) == data_length:
            break
        full_counter += 1
        letters.pop(0)
        letters.append(letter)
    return full_counter


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
