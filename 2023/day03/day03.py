import itertools as it


def bound(value, data):
    return all([0 <= value < len(data), 0 <= value < len(data)])


def main(data):
    number = ""
    number_sum = 0
    for i in range(len(data)):
        j = 0
        while j < len(data[i]):
            offset = 0
            while data[i][j + offset].isdigit():
                number += data[i][j + offset]
                offset += 1
            is_part = False
            if number != "":
                for k, k2 in it.product(range(-1, 2), range(-1, offset + 1)):
                    if (
                        bound(i + k, data)
                        and bound(j + k2, data)
                        and data[i + k][j + k2] != "."
                        and not data[i + k][j + k2].isdigit()
                    ):
                        is_part = True
                        break
            if is_part:
                number_sum += int(number)
            number = ""
            j += offset
            j += 1
    print(f"Part 1: {number_sum}")


def main2(data):
    number_mult = 0
    for i, j in it.product(range(len(data)), range(len(data))):
        numbers = set()
        if data[i][j] == "*":
            for k, k2 in it.product(range(-1, 2), range(-1, 2)):
                if bound(i + k, data) and bound(j + k2, data):
                    if data[i + k][j + k2].isdigit():
                        number = ""
                        back = 0
                        while (
                            bound(j + k2 - back, data)
                            and data[i + k][j + k2 - back].isdigit()
                        ):
                            back += 1
                        forward = 0
                        while (
                            bound(j + k2 + forward, data)
                            and data[i + k][j + k2 + forward].isdigit()
                        ):
                            forward += 1
                        for l in range(-back + 1, forward):
                            number += data[i + k][j + k2 + l]
                        numbers.add(int(number))
            if len(numbers) > 1:
                mult = 1
                for n in numbers:
                    mult *= n
                number_mult += mult
    print(f"Part 2: {number_mult}")

    pass


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    main(lines)
    main2(lines)
