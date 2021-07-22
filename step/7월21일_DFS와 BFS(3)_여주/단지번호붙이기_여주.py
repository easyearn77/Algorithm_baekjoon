import sys

def dfs(x, y, cnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    arr[x][y]=0
    for i in range(4):
        nowx, nowy = x+dx[i], y+dy[i]
        if nowx<0 or nowy<0 or nowx>=n or nowy>=n or not arr[nowx][nowy]:
            continue
        cnt = dfs(nowx, nowy, cnt+1)
    return cnt

n = int(sys.stdin.readline())
arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ans.append(dfs(i, j, 1))
print(len(ans))
for i in sorted(ans):
    print(i)
