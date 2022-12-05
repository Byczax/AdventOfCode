import sys

dice = 0


def main(filename):
    global dice
    players = []
    with open(filename, 'r') as file:
        players = [line.strip() for line in file]
    player1_pos = p1_pos = int(players[0].split()[-1]) - 1
    player2_pos = p2_pos = int(players[1].split()[-1]) - 1

    p1_points = 0
    p2_points = 0
    while True:
        move = roll() + roll() + roll()
        p1_pos = (p1_pos + move) % 10
        p1_points += p1_pos + 1
        if p1_points >= 1000:
            print(p2_points * dice)
            break
        move = roll() + roll() + roll()
        p2_pos = (p2_pos + move) % 10
        p2_points += p2_pos + 1
        if p2_points >= 1000:
            print(p1_points * dice)
            break
    print(player1_pos, player2_pos)
    result = universe_wins(player1_pos, player2_pos, 0, 0)
    print(result)
    print(max(result))


def roll():
    global dice
    dice += 1
    return dice


rolls = [1, 2, 3]
dynamic_table = {}


def universe_wins(p1_pos, p2_pos, p1_points, p2_points):
    global rolls
    if p1_points >= 21:
        return (1, 0)
    if p2_points >= 21:
        return (0, 1)
    if (p1_pos, p2_pos, p1_points, p2_points) in dynamic_table:
        return dynamic_table[(p1_pos, p2_pos, p1_points, p2_points)]
    answer = (0, 0)
    for d1 in rolls:
        for d2 in rolls:
            for d3 in rolls:
                new_p1_pos = (p1_pos + d1 + d2 + d3) % 10
                new_p1_points = p1_points + new_p1_pos + 1
                
                p1, p2 = universe_wins(p2_pos, new_p1_pos, p2_points, new_p1_points)
                answer = (answer[0] + p2, answer[1] + p1)
    dynamic_table[(p1_pos, p2_pos, p1_points, p2_points)] = answer

    return answer


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
