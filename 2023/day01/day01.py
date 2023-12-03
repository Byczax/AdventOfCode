from enum import Enum


class Digits(Enum):
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"


def main(lines):
    number_sum = 0
    for line in lines:
        first = -1
        last = -1
        for character in line:
            if character.isdigit():
                if first == -1:
                    first = character
                last = character
        number = int(f"{first}{last}")
        number_sum += number
    print(f"Part 1: {number_sum}")


def main2(lines):
    number_sum = 0
    for line in lines:
        first = -1
        last = -1
        for i in range(len(line)):
            if line[i].isdigit():
                if first == -1:
                    first = line[i]
                last = line[i]
            for digit in Digits:
                if (line[i : i + len(digit.name)]).upper() == digit.name:
                    if first == -1:
                        first = digit.value
                    last = digit.value
        number = int(f"{first}{last}")
        number_sum += number
    print(f"Part 2: {number_sum}")


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    main(lines)
    main2(lines)
