def solve_grid(board):
        find = search_blank(board)
        if not find:
            return True
        else:
            (row, col) = find
        for i in range(1, 10):
            if check_valid(board, i, (row,col)):
                board[row][col] = i

                if solve_grid(board):
                    return True
                board[row][col] = 0
        return False




def check_valid(board, num, pos):
        for i in range(len(board[0])):  # check for each row
            if board[pos[0]][i] == num and pos[1] != i:  # checking the number inserted matches with any number in the orw and also check if the position is not the exact position of the inserted number
                return False

        for i in range(len(board)):
            if (board[i][pos[1]] == num and pos[0] != i):  # checking the number inserted matches with any number in the coloumn and also check if the position is not the exact position of the inserted number
                return False

        # check each 3X3 box
        x = pos[1] // 3
        y = pos[0] // 3
        for i in range(y * 3, ((y * 3) + 3)):
            for j in range(x * 3, ((x * 3) + 3)):
                if (board[i][j] == num and (i, j) != pos):
                        return False
        return True

def board_print(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print(" | ", end="")
            if j==8:#last line of sudoku
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ",end="")

def search_blank(board):
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if (board[i][j] == 0):
                    return (i, j)
        return None  # no blank squares present i.e. no 0