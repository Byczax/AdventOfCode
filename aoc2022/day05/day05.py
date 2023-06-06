#!/usr/bin/env python3

import sys
import pyperclip
from pathlib import Path
import copy


def read_file(filename: str) -> list:
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [i for i in lines]


def print_and_copy(text: str, result) -> None:
    print(f'{text} - {result}')
    pyperclip.copy(result)
    print(f'{text} Copied to clipboard')
    input('Press enter to continue...')


def main(filename):
    data = read_file(filename)

    stack = []
    commands = []
    all_columns = []
    for line in data:
        if line.startswith('\n'):  # read until there is no more stacks
            break
        stack.append(line)  # add suspect line to list
    for line in data[len(stack)+1:]:
        commands.append(line)  # add commands to list
    for i in range(len(stack[0])):
        # convert lines to columns
        all_columns.append([line[i] for line in stack])

    clean_columns = []
    for line in all_columns:
        if line[-1].isdigit():  # check if line is a stack
            line.reverse()  # reverse the list to properly use pop()
            clean_columns.append(line)  # add line to proper columns
    for line in clean_columns:
        while line[-1] == ' ':  # clean stack from empty spaces
            line.pop()

    print_and_copy('Part 1', part_1(copy.deepcopy(clean_columns), commands))
    print_and_copy('Part 2', part_2(clean_columns, commands))


def part_1(clean_columns, commands):
    result = ""
    for line in commands:
        _, count, _, from_stack, _, to_stack = line.strip().split(' ')
        count, from_stack, to_stack = int(
            count), int(from_stack), int(to_stack)
        for _ in range(count, 0, -1):
            clean_columns[to_stack-1].append(clean_columns[from_stack-1].pop())
    for line in clean_columns:
        result += ''.join(line[-1])
    return result


def part_2(clean_columns, commands):
    result = ""
    for line in commands:
        _, count, _, from_stack, _, to_stack = line.strip().split(' ')
        count, from_stack, to_stack = int(
            count), int(from_stack), int(to_stack)
        # print(count, from_stack, to_stack)
        new_boxes = clean_columns[from_stack-1][-count:]
        for _ in range(count, 0, -1):
            clean_columns[from_stack-1].pop()
        clean_columns[to_stack-1].extend(new_boxes)
    for line in clean_columns:
        result += ''.join(line[-1])
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
