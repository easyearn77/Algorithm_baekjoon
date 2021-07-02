import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

check = [[0] * n for _ in range(n)]

for i in range(n):
    check[i][i] = 1

for i in range(n - 1):
    if numbers[i] == numbers[i + 1]:
        check[i][i + 1] = 1

for l in range(2, n):
    for j in range(n - l):
        if numbers[j] == numbers[j + l] and check[j + 1][j + l - 1] == 1:
            check[j][j + l] = 1

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(check[s - 1][e - 1])
