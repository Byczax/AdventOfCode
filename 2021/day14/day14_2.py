import sys


def main(filename):
    pairs = {}
    chains = {}
    template = ""

    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines]
        template = lines[0]

        # get pair insertion
        for line in lines[2:]:
            key, value = line.split(" -> ")
            pairs[key] = value

    # count patterns in template
    for i in range(len(template)-1):
        pattern = template[i] + template[i+1]
        if pattern not in chains:
            chains[pattern] = 0
        chains[pattern] += 1

    for _ in range(40):
        new_chains = {}
        for key in chains:
            value = pairs[key]
            if key[0] + value not in new_chains:
                new_chains[key[0] + value] = 0
            new_chains[key[0] + value] += chains[key]
            if value + key[1] not in new_chains:
                new_chains[value+key[1]] = 0
            new_chains[value+key[1]] += chains[key]
        chains = new_chains

    letters = {}
    # this loop skip last letter
    for key in chains:
        if key[0] not in letters:
            letters[key[0]] = 0
        letters[key[0]] += chains[key]
    letters[template[-1]] += 1  # but last letter never change

    print(max(letters.values())-min(letters.values()))


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
