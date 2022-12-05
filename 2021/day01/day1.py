import sys

window_size = 3

def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # convert values in array to integers
        int_lines = [int(i) for i in lines]
        print(count_increase(int_lines))
        print(count_increase_window(int_lines))


# count how many times next value is higher than previous
def count_increase(data):
    counter = 0
    previous = data[0]  # first element
    for line in data[1:]:  # get every line, skip first element
        if line - previous > 0:
            counter += 1
        previous = line
    return counter

def count_increase_window(data):
    counter = 0
    for index in range(len(data)-3):
        if sum(data[index+1:index+window_size+1]) - sum(data[index:index+window_size]) > 0:
            counter += 1
    return counter

if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
