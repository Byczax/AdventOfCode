def main(data):
    cube_numbers = {"red": 12, "green": 13, "blue": 14}
    id_sum = 0
    for line in data:
        split = line.split(":")
        game_number = int(split[0].split(" ")[1])
        draws = split[1].split(";")
        validity = True
        for draw in draws:
            cubes = draw.split(",")
            for cube in cubes:
                number, color = cube.strip().split(" ")
                if cube_numbers[color] < int(number):
                    validity = False
        if validity:
            id_sum += game_number
    print(f"Part 1: {id_sum}")


def main2(data):
    power_sum = 0
    for line in data:
        split = line.split(":")
        draws = split[1].split(";")
        minimal_values = {"red": 0, "green": 0, "blue": 0}
        for draw in draws:
            cubes = draw.split(",")
            for cube in cubes:
                number, color = cube.strip().split(" ")
                if minimal_values[color] < int(number):
                    minimal_values[color] = int(number)

        power_sum += (
            minimal_values["red"] * minimal_values["green"] * minimal_values["blue"]
        )
    print(f"Part 2: {power_sum}")
    pass


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    main(lines)
    main2(lines)
