
# 7. 퍼트리기

def spread(board):
    n = len(board)
    clone = []
    for i in range(n):
        row = board[i][:]
        clone.append(row)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i != 0: clone[i-1][j] = 1
                if i != n-1: clone[i+1][j] = 1
                if j != 0: clone[i][j-1] = 1
                if j != n-1: clone[i][j+1] = 1
    return clone

def print_square(board):
    length = len(board)
    for i in range(length):
        for j in range(length):
            print(board[i][j],end=' ')
        print()

board1 = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,1,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
print_square(board1)
print("----------------------------")
board2 = spread(board1)
print_square(board2)
print("----------------------------")
board3 = spread(board2)
print_square(board3)
print("----------------------------")
board4 = spread(board3)
print_square(board4)
print("----------------------------")
board5 = spread(board4)
print_square(board5)
print("----------------------------")

board1 = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,1,0],
         [0,0,0,0,0]]
print_square(board1)
print("----------------------------")
board2 = spread(board1)
print_square(board2)
print("----------------------------")
board3 = spread(board2)
print_square(board3)
print("----------------------------")
board4 = spread(board3)
print_square(board4)
print("----------------------------")
board5 = spread(board4)
print_square(board5)
print("----------------------------")

board1 = [[1,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
print_square(board1)
print("----------------------------")
board2 = spread(board1)
print_square(board2)
print("----------------------------")
board3 = spread(board2)
print_square(board3)
print("----------------------------")
board4 = spread(board3)
print_square(board4)
print("----------------------------")
board5 = spread(board4)
print_square(board5)
print("----------------------------")