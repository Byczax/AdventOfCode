import sys


def main(filename):
    lines = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    cubes = set()
    for i, line in enumerate(lines):
        print(i)
        action, cords = line.split()
        x, y, z = [cord.split("=")[1] for cord in cords.split(",")]
        x_min, x_max = [int(val) for val in x.split("..")]
        y_min, y_max = [int(val) for val in y.split("..")]
        z_min, z_max = [int(val) for val in z.split("..")]
        # if 50 > x_min < -50:
        print(len(cubes))
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max+1):
                for z in range(z_min, z_max+1):
                    if action == "on":
                        cubes.add((x, y, z))
                    else:
                        cubes.discard((x, y, z))


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
