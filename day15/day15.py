import sys
import heapq as heap


def main(filename):
    matrix = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines] # remove newlines (Windows :/ )
        for line in lines:
            array = []
            for element in line:
                array.append(int(element))
            matrix.append(array)
            
    # get result for loaded matrix
    print("Part I:  ", end="")
    find_shortest_path(matrix)
    
    # --------- II Part, bigger map --------------
    new_line = []
    new_matrix = []
    # expand horizontally
    for line in matrix:
        for element in line:
            new_line.append(element) # add old values
        for inc in range(4):
            expansion = [(element+inc) % 9+1 for element in line] # create in new variable
            for element in expansion: # and iterate every element
                new_line.append(element) # to remove ussles array
        new_matrix.append(new_line)
        new_line = []
    
    matrix = new_matrix # save expanded matrix
    new_matrix = [] # prepare for vertical expansion
    # expand vertically
    for line in matrix:
        new_matrix.append(line) # add old values
    for inc in range(4):
        for line in matrix:
            new_matrix.append([(element+inc) % 9+1 for element in line]) # add icemented line
    
    # get result for expanded matrix
    print("Part II: ", end="")
    find_shortest_path(new_matrix)


def find_shortest_path(matrix):
    # AAA, Dijkstra, more at https://github.com/Byczax/SDIZO-Project/tree/master/SDiZO-Projekt_2
    visited = [[0] * len(row) for row in matrix]  # create matrix filled with 0
    vertices = [(0, 0, 0)]  # heap with first vertex
    while(True):
        road, x, y = heap.heappop(vertices)  # pop
        if visited[x][y]:  # if visited, skip
            continue
        if x == y == len(matrix[0])-1:  # if it's our destination
            print(road)
            break
        visited[x][y] = 1  # set vertex to visited state
        for new_x, new_y in [(x-1, y), (x+1, y), (x, y-1), (x, y + 1)]:  # check neighbourhood
            # if in bounds
            if (0 <= new_x < len(matrix[0])) and (0 <= new_y < len(matrix[0])):
                if visited[new_x][new_y]:  # check if visited
                    continue
                # if not visited, then push to heap
                heap.heappush(
                    vertices, (road + matrix[new_x][new_y], new_x, new_y))


if __name__ == "__main__":
    if len(sys.argv) < 2:  # if user didn't give enough arguments, display message
        print("\033[1;32m"
              "Usage: python.exe " + sys.argv[0] + " <filename>"
              "\033[1;m")
        sys.exit(0)
    filename = sys.argv[1]
    main(filename)
