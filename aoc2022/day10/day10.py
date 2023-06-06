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
    part_2(data)
    # print_and_copy('Part 2', part_2(data))


INTERESTING_CYCLES = [20, 60, 100, 140, 180, 220]


def part_1(data):
    cycle = 0
    register_x = 1
    total = 0
    # count = 1
    for value in data:
        if value == "noop":
            cycle += 1
            if cycle in INTERESTING_CYCLES:
                total += register_x * cycle
                print(f'{total} - {register_x} - {cycle} - {register_x * cycle}')
            continue
        else:

            cycle += 1
            if cycle in INTERESTING_CYCLES:
                total += register_x * cycle
                print(f'{total} - {register_x} - {cycle} - {register_x * cycle}')
            cycle += 1
            if cycle in INTERESTING_CYCLES:
                total += register_x * cycle
                print(f'{total} - {register_x} - {cycle} - {register_x * cycle}')
            register_x += int(value.split(" ")[1])
        if cycle > 220:
            break
    return total


def draw_pixel(sprite, cycle, end_string):
    # print(sprite, cycle, end=" - ")
    if cycle % 40 == 0 and cycle != 0:
        end_string.append("\n")
    if sprite - 1 <= cycle % 40 <= sprite + 1:
        # print("X")
        end_string.append("█")
        
    else:
        end_string.append(" ")
        # print(".")
    
    # print(end_string)
    return end_string


def part_2(data):
    sprite = 1
    cycle = 0
    end_string = []
    for value in data:
        draw_pixel(sprite, cycle, end_string)
        if value == "noop":
            cycle += 1
        elif value.split(" ")[0] == "addx":
            cycle += 1
            draw_pixel(sprite, cycle, end_string)
            cycle += 1
            sprite += int(value.split(" ")[1])
        if cycle > 240:
            break
    print("".join(str(x) for x in end_string))
    return end_string


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
