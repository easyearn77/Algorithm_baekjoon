import sys


def multiple_matrix(a, matrix):
    multipled_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                multipled_matrix[i][j] += (matrix[i][k] * a[k][j])
            multipled_matrix[i][j] %= 1000
    return multipled_matrix


def squared(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    elif b % 2:
        s_matrix = squared(a, b - 1)
        squared_matrix = multiple_matrix(a, s_matrix)
        return squared_matrix
    else:
        s_matrix = squared(a, b // 2)
        squared_matrix = multiple_matrix(s_matrix, s_matrix)
        return squared_matrix


a = []
n, b = map(int, sys.stdin.readline().split())
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

re_matrix = squared(a, b)

for arr in re_matrix:
    print(*arr)
