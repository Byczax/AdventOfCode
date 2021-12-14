import sys


def main(filename):
    pairs = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines]
        template = lines[0]
        for line in lines[2:]:
            key, value = line.split(" -> ")
            pairs[key] = value
    print(f"0\t{len(template)}")
    for step in range(10):
        new_template = ""
        for i in range(len(template)-1):
            pattern = template[i] + template[i+1]
            if pattern in pairs:
                if i == 0:
                    new_template += template[i]
                new_template += pairs[pattern] + template[i+1]
        template = new_template
        print(f"{step+1}\t{len(template)}")
    letters = {}
    for letter in template:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    print(max(letters.values()) - min(letters.values()))


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
