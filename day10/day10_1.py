import sys


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        illegal_count = {")": 3, "]": 57, "}": 1197, ">": 25137}
        cases = {"(": ")", "[": "]", "{": "}", "<": ">"}
        points = 0
        for line in lines:
            line = line.replace("\n", "")
            stack = []
            for character in line:
                if character in cases:
                    stack.append(character)
                elif character == cases[stack[-1]]:
                    stack.pop()
                else:
                    points += illegal_count[character]
                    break
        print(points)


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
