board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solver(board):
    find = empty(board)

    if not find:
        return True

    for val in range(1, 10):
        if valid_entry(board, val, find):
            board[find[0]][find[1]] = val
            if solver(board):
                return True
            else:
                board[find[0]][find[1]] = 0

    return False


def valid_entry(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    row = pos[0]
    col = pos[1]
    start_row = 0
    start_col = 0

    if 0 <= row < 3:
        start_row = 0
    elif 3 <= row < 6:
        start_row = 3
    else:
        start_row = 6

    if 0 <= col < 3:
        start_col = 0
    elif 3 <= col < 6:
        start_col = 3
    else:
        start_col = 6

    for i in range(start_row, start_row + 3):
        for j in range(start_col * 3, start_col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("----------------------")
        for col in range(len(board)):
            if col % 3 == 0 and col != 0:
                print("|", end =" ")
            print(board[row][col], end =" ")
        print("")


def empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col
    return None


print_board(board)
solver(board)
print("")
print_board(board)
