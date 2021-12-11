import sys

sum_of_flashes = 0


def main(filename):
    global sum_of_flashes
    created_map = []
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            fix_line = line.replace("\n", "")
            created_map.append([int(i) for i in fix_line])

    for day in range(1000):
        next_day(created_map)
        if sum_of_flashes == len(created_map) * len(created_map[0]):
            print(f"{day+1} \t| {sum_of_flashes}")
            break
        sum_of_flashes = 0

def next_day(squid_map):
    for x in range(len(squid_map)):
            for y in range(len(squid_map[x])):
                squid_map[x][y] += 1
                if squid_map[x][y] == 10:
                    flash(x, y, squid_map)
                    squid_map[x][y] += 1

    for x in range(len(squid_map)):
        for y in range(len(squid_map[x])):
            if squid_map[x][y] > 9:
                squid_map[x][y] = 0
    
def flash(x, y, xy_map):
    global sum_of_flashes
    sum_of_flashes += 1
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if 0 <= i < len(xy_map) and 0 <= j < len(xy_map[0]):
                xy_map[i][j] += 1
                if xy_map[i][j] == 10:
                    flash(i, j, xy_map)
                    xy_map[i][j] += 1


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
