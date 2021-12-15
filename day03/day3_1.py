import sys


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        bits = bit_common(lines)
        bit_number = ""
        for bit_count in bits:
            if bit_count > len(lines)/2:
                bit_number += "1"
            else:
                bit_number += "0"
        inverted_bit_number = ""
        for bit in bit_number:
            if bit == "0":
                inverted_bit_number += "1"
            else:
                inverted_bit_number += "0"
        print(int(bit_number, 2)*int(inverted_bit_number, 2))


def bit_common(data):
    bit_count = []
    for _ in range(len(data[0])-1):
        bit_count.append(0)
    for line in data:
        for bit in range(len(line)-1):
            bit_count[bit] += int(line[bit])
    return bit_count


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
