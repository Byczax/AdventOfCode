import math


def main(data):
    instructions = data[0].strip()
    nodes = {}
    for node in data[2:]:
        node_name, node_pair = node.split(" = ")
        node_1, node_2 = node_pair.replace("(", "").replace(")", "").split(",")
        nodes[node_name.strip()] = (node_1.strip(), node_2.strip())
        pass
    active_node = "AAA"
    number_of_iterations = 0
    while active_node != "ZZZ":
        node_1, node_2 = nodes[active_node]
        direction = instructions[number_of_iterations % len(instructions)]
        if direction == "L":
            active_node = node_1
        else:
            active_node = node_2
        number_of_iterations += 1
    print("Part 1: ", number_of_iterations)


def main2(data):
    instructions = data[0].strip()
    start_nodes = set()
    nodes = {}

    for node in data[2:]:
        node_name, node_pair = node.split(" = ")
        node_1, node_2 = node_pair.replace("(", "").replace(")", "").split(",")
        node_last_letter = node_name.strip()[-1]
        if node_last_letter == "A":
            start_nodes.add(node_name.strip())
        nodes[node_name.strip()] = (node_1.strip(), node_2.strip())
        pass

    end_node_iterations = []
    for node in start_nodes:
        number_of_iterations = 0
        while node[-1] != "Z":
            node_1, node_2 = nodes[node]
            direction = instructions[number_of_iterations % len(instructions)]
            if direction == "L":
                node = node_1
            else:
                node = node_2
            number_of_iterations += 1
        end_node_iterations.append(number_of_iterations)
    print("Part 2: ", math.lcm(*end_node_iterations))
    pass


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    main(lines)
    main2(lines)
