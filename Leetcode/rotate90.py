matrix =[[1,2,3],[4,5,6],
        [7,8,9]]

print(matrix)
def rotate_90(m):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            matrix[j][(n-1)-i] = matrix[i][j]
        print()
    return matrix
            

print(rotate_90(matrix))

