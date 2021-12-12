import sys


def main(filename):
    connections = {}
    path = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            a, b = line.replace("\n", "").split("-")
            if a not in connections:
                connections[a] = []
            if b not in connections:
                connections[b] = []

            connections[a].append(b)
            connections[b].append(a)

    queue = [["start", set(["start"]), False]]

    while queue.count > 0:
        position, visited, twice = queue.pop(0)
        if position == "end":
            path += 1
            continue
        for point in connections[position]:
            if point not in visited:
                new_visited = set(visited)
                if not point.isupper():
                    new_visited.add(point)
                queue.append([point, new_visited, twice])
            elif point in visited and twice is False and point not in ["start", "end"]:
                queue.append([point, visited, True])

    print(path)


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
