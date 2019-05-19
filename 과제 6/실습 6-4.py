#전치행렬 구하기
def transpose(mat):
    no_of_columns = len(mat[0])
    no_of_row = len(mat)
    transposed = []
    print(transposed)
    for i in range(no_of_columns):
        transposed.append([])
        for j in range(no_of_row):
            transposed[i].append(mat[j][i])
    return transposed


m   =  [[1, 0, 0, 0],
        [0, 1, 0, 1]]


print(transpose(m))