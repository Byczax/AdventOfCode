import sys

heightmap = []


def main(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            heightmap.append([int(i) for i in line.replace("\n", "")])
    mul_basin = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            basin_size = 0
            if all(get_conditions(i, j)):
                basin_points = []
                visited_points = {(i, j)}
                basin_size += 1
                [basin_points.append(e) for e in [
                    (i+1, j), (i-1, j), (i, j+1), (i, j-1)]]
                while len(basin_points) > 0:
                    a, b = basin_points.pop(0)
                    if (a, b) in visited_points:
                        continue
                    visited_points.add((a, b))
                    if 0 <= a < len(heightmap) and 0 <= b < len(heightmap[0]):
                        if heightmap[a][b] != 9:
                            basin_size += 1
                            [basin_points.append(e) for e in [
                                (a+1, b), (a-1, b), (a, b+1), (a, b-1)]]
                mul_basin.append(basin_size)
    mul_basin.sort()
    print(mul_basin[-1] * mul_basin[-2] * mul_basin[-3])


def get_conditions(i, j):
    conditions = []
    if len(heightmap)-1 < i < 0 or len(heightmap[0])-1 < j < 0:
        return False
    if i == 0:
        conditions.append(True)
    else:
        conditions.append(heightmap[i][j] < heightmap[i-1][j])
    if i == len(heightmap) - 1:
        conditions.append(True)
    else:
        conditions.append(heightmap[i][j] < heightmap[i+1][j])
    if j == 0:
        conditions.append(True)
    else:
        conditions.append(heightmap[i][j] < heightmap[i][j-1])
    if j == len(heightmap[0]) - 1:
        conditions.append(True)
    else:
        conditions.append(heightmap[i][j] < heightmap[i][j+1])
    return conditions


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
