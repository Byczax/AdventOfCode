import sys

code = []
def main(filename):
    lines = []
    global code
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    code = lines[0]
    pixels = set()
    
    for x, line in enumerate(lines[2:]):
        for y, pixel in enumerate(line):
            if pixel == "#":
                pixels.add((x, y))
    display(pixels)
    for iteration in range(51):
        print(f"{iteration+1}\t{len(pixels)}")
        pixels = step(pixels, iteration%2==0)
        # display(pixels)
def step(pixels, on):
    offset = 5
    new_pixels = set()
    x_min = min([x for x, _ in pixels])
    x_max = max([x for x, _ in pixels])
    y_min = min([y for _, y in pixels])
    y_max = max([y for _, y in pixels])
    for x in range(x_min - 5, x_max + 10):
        for y in range(y_min - 5, y_max + 10):
            value = 0
            bit = 8
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if ((x+dx, y+dy) in pixels) == on:
                        value += 2**bit
                    bit -= 1
            if (code[value] == "#") != on:
                new_pixels.add((x,y))
    return new_pixels
                
def display(pixels):
    offset = 5
    x_min = min([x for x, _ in pixels])
    x_max = max([x for x, _ in pixels])
    y_min = min([y for _, y in pixels])
    y_max = max([y for _, y in pixels])
    for x in range(x_min - offset, x_max + offset):
        row = "."
        for y in range(y_min - offset, y_max + offset):
            if (x,y) in pixels:
                row += "#"
            else:
                row += "."
        print(row)    

if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
