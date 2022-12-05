import sys


def main(filename):
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    print(part1(lines))
    print(part2(lines))


def part1(data):

    def bit_common(data):
        bit_count = []
        for _ in range(len(data[0])-1):
            bit_count.append(0)
        for line in data:
            for bit in range(len(line)-1):
                bit_count[bit] += int(line[bit])
        return bit_count

    bits = bit_common(data)
    bit_number = ""
    for bit_count in bits:
        if bit_count > len(data)/2:
            bit_number += "1"
        else:
            bit_number += "0"
    inverted_bit_number = ""
    for bit in bit_number:
        if bit == "0":
            inverted_bit_number += "1"
        else:
            inverted_bit_number += "0"
    return int(bit_number, 2)*int(inverted_bit_number, 2)


def part2(data):
    def test_numbers(data, common):

        def bit_common(data):
            bit_count = []
            for _ in range(len(data[0])-1):
                bit_count.append([0, 0])
            for line in data:
                for bit in range(len(line)-1):
                    bit_count[bit][int(line[bit])] += 1
            return bit_count

        test_bit = "1"
        for bit in range(len(data[0])-1):
            bits = bit_common(data)
            if bits[bit][1] == 0:
                test_bit = "0"
            elif bits[bit][0] == 0:
                test_bit = "1"
            else:
                if bits[bit][0] > bits[bit][1]:
                    test_bit = "1"
                else:
                    test_bit = "0"
                if not common:
                    if test_bit == "1":
                        test_bit = "0"
                    else:
                        test_bit = "1"
            new_lines = []
            for line in data:
                if line[bit] == test_bit:
                    new_lines.append(line)
            data = new_lines
        return int(data[0], 2)
    
    num1 = test_numbers(data, True)
    num2 = test_numbers(data, False)
    return num1 * num2


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
