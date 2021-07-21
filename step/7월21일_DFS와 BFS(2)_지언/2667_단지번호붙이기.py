
graph = []
n = int(input())
answer = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
for _ in range(n):
    x = list(map(int, input()))
    graph.append(x)


def dfs(x, y):
    global cnt
    graph[x][y] = '#'
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            graph[nx][ny] = '#'
            dfs(nx, ny)
    return cnt


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            answer.append(dfs(i, j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)
