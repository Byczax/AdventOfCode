import sys


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        bingo_numbers = lines[0].split(",")  # get bingo numbers
        bingo_numbers = [int(i) for i in bingo_numbers]  # change string to int
        # skip first 2 lines because they don't have boards
        boards = get_bingo_boards(lines[2:])
        last_win_board = boards[0]  # create temp variable for boards
        last_called_number = 0  # save winning number for "losing" board
        bingo_found = False  # for part 1
        for bingo_number in bingo_numbers:
            remove_boards = []  # array for saving array to remove
            for board_number in range(len(boards)):
                # 1. Remove called number from boards
                boards[board_number] = delete_number(
                    boards[board_number], bingo_number)
                # 2. Check if any board have already bingo
                if check_bingo(boards[board_number]):
                    # For Part II
                    # 1. Set winning board as last winned
                    last_win_board = boards[board_number]
                    # 2. Save called number
                    last_called_number = bingo_number
                    # 3. Save board index for future removal
                    remove_boards.append(board_number)
                    # For Part I
                    if not bingo_found:  # if it's first winning board
                        print("Wining board points: ", end="")
                        # cound and display points
                        print(count_points(boards[board_number], bingo_number))
                        bingo_found = True  # save that's we already found winning board
            # For Part II
            # reverse to avoid out of bounds
            for number in reversed(remove_boards):
                del boards[number]  # 4. Remove redundant boards from list
        print("Losing board points: ", end="")
        # 5. display "losing" board points
        print(count_points(last_win_board, last_called_number))


# use when found bingo, count board points
def count_points(board, multiplayer):
    points = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:  # check if number is not used
                points += board[i][j]
    return points * multiplayer


# check if board have bingo
def check_bingo(board):
    for i in range(5):
        sum_x = 0
        sum_y = 0
        for j in range(5):
            sum_x += board[i][j]
            sum_y += board[j][i]
        # is sum any of the rows or columns equals -5, that means that board have bingo
        if(sum_x == -5 or sum_y == -5):
            return True
    return False


# print board for tests
def print_board(board):
    for line in board:
        print(line)
    print()


# delete called number from board
def delete_number(board, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = -1  # use -1 for already called numbers
    return board


# get boards from file
def get_bingo_boards(data):
    boards = []
    for line in range(0, len(data), 6):
        boards.append(get_bingo_board(data[line:line+5]))
    return boards


# convert given data to board
def get_bingo_board(data):
    board = []
    for line in data:
        column_values = []
        line = line.replace("  ", " ")  # remove artefacts
        # remove endline from last numbers in row
        splitted = line.replace("\n", "").split(" ")
        for element in splitted:
            if element == "":  # empty element is created when it's align first element in file
                continue
            column_values.append(int(element))  # create rows
        board.append(column_values)  # create board
    return board


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
