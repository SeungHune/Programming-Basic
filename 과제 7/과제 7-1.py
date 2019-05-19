import random

# 보드만들기
def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    s1 = [seed[0], seed[1], seed[2], seed[3], seed[4], seed[5]]
    s2 = [seed[5], seed[3], seed[4], seed[1], seed[0], seed[2]]
    s3 = [seed[1], seed[2], seed[3], seed[0], seed[5], seed[4]]
    s4 = [seed[4], seed[0], seed[5], seed[2], seed[1], seed[3]]
    s5 = [seed[2], seed[4], seed[1], seed[5], seed[3], seed[0]]
    s6 = [seed[3], seed[5], seed[0], seed[4], seed[2], seed[1]]
    board = [s1, s2, s3, s4, s5, s6]
    return board

#섞기
def transpose(board):
    transposed = []
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        i = -1
        for a in row:
            i = i + 1
            transposed[i].append(a)
    return transposed

#난이도 선택
def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if (level == "하"):
        return 5
    elif(level == "중"):
        return 12
    elif(level == "상"):
        return 20

#빈칸 만들기
def make_holes(board,no_of_holes):
    holeset = set()
    while (len(holeset) <= no_of_holes -1 ):
        i = random.randint(0,5)
        j = random.randint(0,5)
        if (board[i][j] == 0):
            continue
        else:
            board[i][j] = 0
            holeset.add((i+1,j+1))
    return (board, holeset)

#보드 보이기
def show_board(board):
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    i = 1
    for row in board:
        row = str(row)
        row = row.replace(",","")
        row = row.replace("[","")
        row = row.replace("]","")
        row = row.replace("0",".")
        print(i, "|", row)
        i = i +1
    print()

#정답 받기
def get_integer(message,i,j):
    number = input(message)
    while not (int(number) >= i and int(number) <=j):
        number = input(message)
    return int(number)

#복사하기
def copy_board(board):
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone

def sudok():
    a = get_level()
    ans_board = transpose(transpose(create_board()))
    solution = copy_board(ans_board)
    c,hole = make_holes(ans_board,a)
    show_board(c)
    while True:
        row = get_integer("가로줄번호(1~6): ", 1, 6)
        col = get_integer("세로줄번호(1~6): ", 1, 6)
        ans = int(input("들어갈 숫자는? : "))
        if (ans_board[row-1][col-1] != 0):
            print("빈자리가 아닙니다.")
            show_board(c)
        elif (int(solution[row-1][col-1]) == ans):
            print("맞았습니다!")
            c[row-1][col-1] = ans
            show_board(c)
            hole = hole - {(row,col)}
        else:
            print("틀렸습니다!")
            show_board(c)
        if (hole == set()):
            print("완성했습니다~~")
            break
sudok()
