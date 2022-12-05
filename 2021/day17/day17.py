import sys
import heapq as heap


def main(filename):
    the_best_y = 0
    count_velocities = 0
    with open(filename, 'r') as file:
        lines = file.read().strip()

        str_x, str_y = lines.split(":")[-1].split(", ")
        min_x, max_x = str_x.split("=")[-1].split("..")
        min_y, max_y = str_y.split("=")[-1].split("..")
        min_x, max_x, min_y, max_y = int(min_x), int(
            max_x), int(min_y), int(max_y)
        print(min_x, max_x, min_y, max_y, sep=" | ")

        for start_x in range(max_x + 1):
            for start_y in range(min_y, max_x+1):
                print(start_x, start_y)
                got_it = False
                best_y = 0
                x, y = 0, 0
                pos_x, pos_y = start_x, start_y
                for _ in range(1000):
                    x += pos_x
                    y += pos_y
                    best_y = max(best_y, y)
                    if pos_x > 0:
                        pos_x -= 1
                    elif pos_x < 0:
                        pos_x += 1
                    pos_y -= 1
                    if x > max_x or y < min_y:
                        break

                    if min_x <= x <= max_x and min_y <= y <= max_y:
                        got_it = True
                        break

                if got_it:
                    count_velocities += 1
                    if the_best_y < best_y:
                        the_best_y = best_y
                        print(start_x, start_y, the_best_y, count_velocities)
        print(f"Part I: {the_best_y}, Part II: {count_velocities}")


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
