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

    print_and_copy('Part 1', part_1(data))
    # print_and_copy('Part 2', part_1_2(data[0], 14))


def count_size(data, directory, directories):
    total = 0
    for element in data[directory]:
        if element[1] == "dir":
            if element[0] in directories:
                total += directories[element[0]]
            else:
                total += count_size(data, element[0], directories)
        else:
            total += int(element[1])
    return total


def part_1(data):
    struct = {'~': 0}
    active_dir = ['~']

    for line in data:
        if line.startswith('$ cd '):
            if line[5:][0] == '/':
                active_dir = ['~']
            elif line[5:] == '..':
                active_dir = active_dir[:-1]
            else:
                active_dir.append(line[5:])
        elif line == '$ ls':
            pass
        else:
            if line.startswith('dir '):
                struct['/'.join(active_dir) +
                       '/' + line[4:]] = 0
            else:
                size = int(line.split(' ')[0])

                for index in range(len(active_dir)):
                    struct['/'.join(active_dir[:index + 1])] += size

    result = sum(v for k, v in struct.items() if v < 100000)
    print_and_copy('Part 1', result)
    needed = 30000000 - (70000000 - struct['~'])
    result = min(v for k, v in struct.items() if v > needed)
    return result


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
