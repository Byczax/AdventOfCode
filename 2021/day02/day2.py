import sys


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(count_position(lines))
        print(count_position_2(lines))


# count how many times next value is higher than previous
def count_position(data):
    coordinates = {}
    for line in data:
        position, value = line.split(" ")
        if position not in coordinates:
            coordinates[position] = 0
        coordinates[position] += int(value)
    horizontal = coordinates["forward"]
    depth = coordinates["down"] - coordinates["up"]
    return horizontal * depth


def count_position_2(data):
    params = {
        "depth": 0,
        "horizontal": 0,
        "aim": 0
    }
    for line in data:
        position, value = line.split(" ")
        value = int(value)
        if position == "forward":
            params["horizontal"] += value
            if params["aim"] != 0:
                params["depth"] += value * params["aim"]
        elif position == "down":
            params["aim"] += value
        else:
            params["aim"] -= value

    return params["depth"] * params["horizontal"]


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
