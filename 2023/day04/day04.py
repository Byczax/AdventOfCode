from collections import defaultdict


def main(data):
    total = 0
    for line in data:
        winning, owned = line.split("|")
        numbers = set()
        count = -1
        for number in winning.split(":")[1].strip().split():
            numbers.add(int(number))
        for number in owned.strip().split():
            if int(number) in numbers:
                count += 1
        if count == 0:
            total += 1
        elif count > 0:
            total += 2**count
    print(f"Part 1: {total}")
    pass


def main2(data):
    total = 0
    scratchcards = defaultdict(int)
    for i in range(len(data)):
        scratchcards[i] += 1
        winning, owned = data[i].split("|")
        numbers = set()
        count = 0
        for number in winning.split(":")[1].strip().split():
            numbers.add(int(number))
        for number in owned.strip().split():
            if int(number) in numbers:
                count += 1
        for j in range(count):
            scratchcards[j + i + 1] += 1 * scratchcards[i]
    total = sum(scratchcards.values())
    print(f"Part 2: {total}")
    pass


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    main(lines)
    main2(lines)
