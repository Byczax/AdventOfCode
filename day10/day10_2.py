import sys


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        case_value = {")": 1, "]": 2, "}": 3, ">": 4}
        cases = {"(": ")", "[": "]", "{": "}", "<": ">"}
        points = []
        for line in lines:
            line = line.replace("\n", "")  # shit, windows
            stack = []
            error = False
            for character in line:
                if character in cases:
                    stack.append(character)
                elif character == cases[stack[-1]]:
                    stack.pop()
                else:
                    error = True
                    break
            if not error:
                loop_points = 0
                while len(stack) > 0:
                    case = stack.pop()
                    loop_points *= 5
                    loop_points += case_value[cases[case]]
                points.append(loop_points)
        points.sort()
        print(points[len(points) // 2])


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
