import random
def make_holes(board,no_of_holes):
    holeset = set()
    while (len(holeset) <= no_of_holes -1 ):
        i = random.randint(0,3)
        j = random.randint(0,3)
        if (board[i][j] == 0):
            continue
        else:
            board[i][j] = 0
            holeset.add((i+1,j+1))
    return (board, holeset)


board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(make_holes(board,3))
# 알고리즘
# parameter: 정답 보드 board, 빈칸수 no_of_holes
# return: 퍼즐 보드 board, 빈칸좌표 집합 holeset
# 1. holeset을 공집합으로 초기화
# 2. no_of_holes 만큼 빈칸을 만들때까지 다음을 계속
# 2.1 i = 무작위로 0,1,2,3 중에 하나를 가로줄 번호로 선정
# 2.2 j = 무작위로 0,1,2,3 중에 하나를 세로줄 번호로 선정
# 2.3 board에서 가로줄번호 i, 세로줄번호 j 위치좌표 (i,j)의 값을 0으로 변경
# 2.4 board에서 (i,j) 위치에 이미 0이 있으면 무효
# 2.5 holeset 집합에 (i,j) 추가
