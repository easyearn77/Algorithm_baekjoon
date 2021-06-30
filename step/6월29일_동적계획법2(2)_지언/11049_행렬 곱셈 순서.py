import sys

n = int(sys.stdin.readline())
array = []
for i in range(n):
    r, c = map(int, sys.stdin.readline().split())
    array.append((r, c))
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(0, n - i):
        if i == 1:
            matrix[j][j + i] = array[j][0] * array[j][1] * array[j + i][1]
            continue

        matrix[j][j + i] = 2 ** 32  # 최댓값
        for k in range(j, j + i):
            matrix[j][j + i] = min(matrix[j][j + i],
                                   matrix[j][k] + matrix[k + 1][j + i] + array[j][0] * array[k][1] * array[j + i][1])
print(matrix[0][n - 1])
