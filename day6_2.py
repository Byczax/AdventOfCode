import sys


def main(filename, day):
    with open(filename, 'r') as file:
        line = file.readlines()
        fishes = {}
        str_numbers = line[0].split(",")
        # convert values in array to integers
        int_numbers = [int(i) for i in str_numbers]
        for i in range(9):
            fishes[i] = 0
        for number in int_numbers:
            fishes[number] += 1
        for _ in range(int(day)):
            temp = fishes[0]
            for i in range(8):
                fishes[i] = fishes[i+1]
            fishes[6] += temp
            fishes[8] = temp
        print(sum(fishes.values()))


if __name__ == "__main__":
    if len(sys.argv) < 3:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename> <day>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    day = sys.argv[2]
    main(filename, day)
