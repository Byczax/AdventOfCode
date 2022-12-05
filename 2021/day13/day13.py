import sys

window_size = 3


def main(filename):
    point_list = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines]
        instruction_list = []
        for line in lines:
            if line == "":
                for instruction in lines[lines.index(line)+1:]:
                    instruction_list.append(instruction.split()[-1].split("="))
                break
            point_list.append([int(i) for i in line.split(",")])

    print_part1 = True
    for value in instruction_list:
        new_point_list = []
        check_cord = (True if value[0] == "y" else False)  # check, fold x or y

        for point in point_list:
            if point[check_cord] > int(value[1]):
                if check_cord:
                    new_point = [point[0], -point[1]+2*int(value[1])]
                else:
                    new_point = [-point[0]+2*int(value[1]), point[1]]

                if new_point not in new_point_list:
                    new_point_list.append(new_point)
            elif point not in new_point_list:
                new_point_list.append(point)
        point_list = new_point_list

        if print_part1:
            print(len(point_list), end="\n\n")
            print_part1 = False

    max_x = max([x for [x, _] in point_list])
    max_y = max([y for [_, y] in point_list])

    result = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            result += ("█" if [x, y] in point_list else " ")
        print(result)
        result = ""


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
