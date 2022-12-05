import sys


def main(filename):
    heightmap = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            heightmap.append([int(i) for i in line.replace("\n", "")])
    risk_level = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            conditions = []
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

            if all(conditions):
                risk_level += 1 + heightmap[i][j]
    print(risk_level)


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
