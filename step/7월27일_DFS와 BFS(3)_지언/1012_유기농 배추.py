import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global graph
    graph[y][x] = '#'
    queue = [[x, y]]
    while queue:
        x=queue[0][0]
        y=queue[0][1]
        del queue[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = '#'
                queue.append([nx, ny])
    return 0


t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    for j in range(n):
        for i in range(m):
            if graph[j][i] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)
