import sys


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        position = count_position(lines)
        print(position)
        horizontal = position["forward"]
        depth = position["down"] - position["up"] 
        print(horizontal * depth)


# count how many times next value is higher than previous
def count_position(data):
    coordinates = {}
    for line in data:
        position, value = line.split(" ")
        if position not in coordinates:
            coordinates[position] = 0
        coordinates[position] += int(value)
    return coordinates


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
