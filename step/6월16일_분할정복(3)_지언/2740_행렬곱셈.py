import sys

a = []
b = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
m, k = map(int, sys.stdin.readline().split())
for _ in range(m):
    b.append(list(map(int, sys.stdin.readline().split())))

ans = [[0 for _ in range(k)] for row in range(n)]
for i in range(n):
    for j in range(k):
        for t in range(m):
            ans[i][j]+=a[i][t]*b[t][j]

for i in range(n):
    for j in range(k):
        print(ans[i][j],end=' ')
    print()