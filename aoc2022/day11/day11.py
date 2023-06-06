#!/usr/bin/env python3

import sys
import pyperclip
from pathlib import Path
# import sys
# sys.setrecursionlimit(100000)

class money:
    items: list
    multiplier: int
    test: int
    test_true: int
    test_false: int

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
    # part_2(data)
    # print_and_copy('Part 2', part_2(data))


INTERESTING_CYCLES = [20, 60, 100, 140, 180, 220]


def part_1(data):
    monkeys = []
    active_monkey = None
    for line in data:
        if line.startswith("Monkey"):
            monkeys.append(money())
            active_monkey = int(line.split(" ")[1].replace(":", ""))
        elif line.startswith("Starting items"):
            monkeys[active_monkey].items = [int(i.replace(",","")) for i in line.split(" ")[2:]]
            
                
            

        
    return total








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
