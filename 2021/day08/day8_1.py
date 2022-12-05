import sys


def main(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            input_digits, output_digits = line.replace("\n", "").split(" | ")
            for digit in output_digits.split():
                if len(digit) in [2, 3, 4, 7]:
                    count += 1
        print(count)


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
