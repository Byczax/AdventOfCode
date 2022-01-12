import sys
import heapq as heap


def add(pair1, pair2):
    return [pair1, pair2]


def reduce(pairs):
    pass

def explode(pairs):
    pass

def split(pairs):
    pass

def magnitude(elements):
    if len(elements) > 1:
        return 3*magnitude(elements[0]) + 2*magnitude(elements[1])
    else:
        return elements[0]

def main(filename):
    lines = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
        
    addition = None
    for line in lines:
        # print(line)
        addition = add(addition, line)
        print(addition)
        

if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
