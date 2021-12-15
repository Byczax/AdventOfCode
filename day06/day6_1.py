import sys


def main(filename, day):
    with open(filename, 'r') as file:
        line = file.readlines()
        str_numbers = line[0].split(",")
        # convert values in array to integers
        int_numbers = [int(i) for i in str_numbers]
        for _ in range(int(day)):
            for i in range(len(int_numbers)):
                if int_numbers[i] == 0:
                    int_numbers.append(8)
                    int_numbers[i] = 6
                else:
                    int_numbers[i] -= 1
        print(len(int_numbers))
                    



if __name__ == "__main__":
    if len(sys.argv) < 3:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename> <day>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    day = sys.argv[2]
    main(filename, day)
