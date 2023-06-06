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
    points = {
        "X": 1,
        "Y": 2,
        "Z": 3,

        "A X": 3,
        "A Y": 6,
        "A Z": 0,

        "B X": 0,
        "B Y": 3,
        "B Z": 6,

        "C X": 6,
        "C Y": 0,
        "C Z": 3
    }
    total_points = sum([points[line.split(" ")[1]] + points[line]
                       for line in data])

    print_and_copy('Part 1', total_points)

    points = {
        "A X": 3,  # rock beats scissors
        "B X": 1,  # paper beats rock
        "C X": 2,  # scissors beats paper

        "A Y": 4,  # rock draws rock
        "B Y": 5,  # paper draws paper
        "C Y": 6,  # scissors draws scissors

        "A Z": 8,  # rock loses to paper
        "B Z": 9,  # paper loses to scissors
        "C Z": 7  # scissors loses to rock
    }

    total_points = sum([points[i] for i in data])

    print_and_copy('Part 2', total_points)


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
