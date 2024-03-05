def main(data):
    times = [int(x) for x in data[0].split()[1:]]
    distances = [int(x) for x in data[1].split()[1:]]
    mult_answer = 1
    for time, distance in zip(times, distances):
        beaten_number = 0
        print("Initial:", time, distance)
        for i in range(1, time):
            if (time - i) * i > distance:
                beaten_number += 1
        print("Beaten:", beaten_number)
        mult_answer *= beaten_number
    print(f"Part 1: {mult_answer}")
    pass


def main2(data):
    time = int(data[0].replace(" ", "").split(":")[1])
    distance = int(data[1].replace(" ", "").split(":")[1])
    print("Initial:", time, distance)
    beaten_number = 0
    for i in range(1, time):
        if (time - i) * i > distance:
            beaten_number += 1
    print(f"Part 2: {beaten_number}")
    pass


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    main(lines)
    main2(lines)
