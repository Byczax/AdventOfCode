import sys
from itertools import permutations

LETTER_STRING = "abcdefg"


def main(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

        digit_map = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
                     "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
        # convert to dict for easy comparsion
        digit_set = set(digit_map)

        sum_all = 0

        for line in lines:
            input_digits, output_digits = line.replace("\n", "").split(" | ")
            input_digits, output_digits = input_digits.split(), output_digits.split()

            for permutation in permutations(LETTER_STRING):
                # get par permutation
                digit_dict = {i: letter for i, letter in zip(
                    permutation, LETTER_STRING)}
                # get line code, sort to get same order as digit_map
                output_dict = {"".join(sorted(map(digit_dict.get, q)))
                               for q in input_digits}
                # check if code is correct
                if digit_set == output_dict:
                    # if correct, get output digits, sort to get same order as digit_map
                    result = ["".join(sorted(map(digit_dict.get, q)))
                              for q in output_digits]
                    # decode
                    result = "".join(str(digit_map.index(q)) for q in result)
                    sum_all += int(result)  # add to sum
        print(sum_all)


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
