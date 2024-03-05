from collections import defaultdict
import itertools as it
import math
from functools import reduce

def find_next_value(sequence):
    last_value = sequence[-1]
    last_values = [last_value]
    first_values = [sequence[0]]
    while last_value:
        reduced_sequence = [y-x for x,y in list(zip(sequence[:-1], sequence[1:]))]
        last_value = reduced_sequence[-1]
        first_value = reduced_sequence[0]
        
        last_values.append(last_value)
        first_values.append(first_value)
        sequence = reduced_sequence
    predicted = reduce(lambda x,y: y-x, list(reversed(first_values)))
    return sum(last_values), predicted

def main(data):
    result_sum_1 = 0
    result_sum_2 = 0
    for line in data:
        part_1, part_2 = find_next_value([int(x) for x in line.split()])
        result_sum_1 += part_1
        result_sum_2 += part_2
    print(result_sum_1, result_sum_2)
    pass


# def main2(data):
#     print("PART 2")
#     result_sum = 0
#     for line in data:
#         values = [int(x) for x in line.split()]
#         reversed_values = list(reversed(values))
#         print("===",reversed_values)
#         result_sum += find_next_value(reversed_values)
#     print(result_sum)
#     pass

#     pass


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    main(lines)
    # main2(lines)
