#!/usr/bin/env python3

import sys
sys.path.append('..')  # for
from utils import utils


def main(filename: str):
    file_data = utils.read_file(filename)
    food_count = 0
    biggest_count = []
    for data in file_data:
        if data == '':
            biggest_count.append(food_count)
            food_count = 0
        else:
            food_count += int(data)
    biggest_count.append(food_count)
    biggest_count.sort(reverse=True)
    utils.print_and_copy('Part 1', biggest_count[0])
    utils.print_and_copy('Part 2', sum(biggest_count[:3]))


if __name__ == "__main__":
    main(utils.read_user_input_or_exit())
