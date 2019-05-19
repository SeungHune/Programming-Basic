#행렬안에 중복된정수 여부(스도쿠)
def issudoku(mat):
    matlist = []
    size = len(mat)
    for i in range(size):
        for j in range(size):
            matlist.append(mat[i][j])
    matlist = sorted(matlist)
    while (matlist != []):
        if len(matlist) == 1:
            break
        if (matlist[0] == matlist[1]):
            return False
        else:
            matlist = matlist[1:]
    return True

matt = [[ 1, 2,  3, 4],
         [ 8, 7,  6,  5],
         [ 9, 10, 11,  12],
         [16, 15,  14,  13]]
mat =  [[1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 1]]
ma =     [[ 1, 9,  5, 11],
         [ 9, 4,  7,  3],
         [ 5, 7, -7,  8],
         [11, 3,  8,  6]]
mattt =  [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
print(issudoku(matt))
print(issudoku(mat))
print(issudoku(ma))
print(issudoku(mattt))


