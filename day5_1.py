import sys


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        # create two dimensional array
        # DON'T DO array = [[0] * SIZE] * SIZE
        pipe_map = []
        max_size = 999
        for _ in range(max_size):
            line = []
            for _ in range(max_size):
                line.append(0)
            pipe_map.append(line)

        for line in lines:
            xy1, xy2 = line.split(" -> ")
            x1, y1 = xy1.split(",")
            x2, y2 = xy2.split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            if x1 == x2:  # check for vertical line
                if y1 > y2:  # range need start value be bigger than end value
                    y1, y2 = y2, y1  # swap
                for i in range(y1, y2+1):
                    pipe_map[i][x1] += 1
            elif y1 == y2:  # check for horizontal line
                if x1 > x2:  # range need start value be bigger than end value
                    x1, x2 = x2, x1  # swap
                for i in range(x1, x2+1):
                    pipe_map[y1][i] += 1
        count_hazards = 0
        for row in pipe_map:
            for element in row:
                if element > 1:
                    count_hazards += 1
        print(count_hazards)


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
