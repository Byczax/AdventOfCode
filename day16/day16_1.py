from os import sep
import sys


def main(filename):
    line = ""
    with open(filename, 'r') as file:
        lines = file.readlines()
        line = [line.replace("\n", "")
                for line in lines]  # remove newlines (Windows :/ )
        line = line[0]

    binary_line = ""
    for element in line:
        binary_line += bin(int(element, 16))[2:].zfill(4)
    print(binary_line, end="\n\n")

    result = parse(binary_line)
    print(result)

    print(version_sum(result))


def version_sum(result):
    all_sum = result[0]
    print(result)
    if result[1] == 4:
        return all_sum
    else:
        return all_sum + version_sum(result[2][0])


def parse(bits):
    
    version, bits = int(bits[:3], 2), bits[3:]

    type_id, bits = int(bits[:3], 2), bits[3:]
    
    if type_id == 4:
        data = []
        
        while True:
            prefix, bits = bits[0], bits[1:]
            data += bits[:4]
            bits = bits[4:]
            if prefix == "0":
                break
            
        data = "".join([i for i in data])
        return (version, type_id, int(data, 2))
    
    else:
        packets = []
        length_id, bits = bits[0], bits[1:]
        print(version, type_id, length_id, sep="~")
        if length_id == "0":
            packet_length, bits = int(bits[:15], 2), bits[15:]
            packet, bits = bits[:packet_length], bits[packet_length:]
            print(packet_length)
            while packet:
                print(packet)
                packets.append(parse(packet))
        else:
            packet_number, bits = int(bits[:11], 2), bits[11:]
            for _ in range(packet_number):
                packets.append(parse(bits))
        return (version, type_id, packets)


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
