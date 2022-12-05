import sys


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        str_values = lines[0].split(",")
        # convert values in array to integers
        int_values = [int(i) for i in str_values]
        max_value = max(int_values)  # get max existing value
        # create dict with size = max existing value
        all_values = {}
        for i in range(max_value + 1):
            all_values[i] = 0
        # count all number types
        for number in int_values:
            all_values[number] += 1
        best_fuel = sys.maxsize
        # iterate all posible alignments
        for align in range(max_value + 1):
            fuel = 0
            good = True
            # iterate all values in dict
            for i in range(max_value + 1):
                # calculate cost for 1 crab
                align_cost = calc_sum(abs(align - i))
                # multiply cost by all crabs with this position
                fuel += align_cost * all_values[i]
                # limiter, stop calculating when fuel is already inferior
                if fuel > best_fuel:
                    good = False
                    break
            # check if calculated value is better
            if good and fuel < best_fuel:
                best_fuel = fuel  # save
        print(best_fuel)


# function for calculating needed fuel
def calc_sum(value):
    return (value*(value+1))//2


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
