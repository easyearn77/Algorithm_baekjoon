import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1


def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visit[v] = 0
    while len(queue)>0:
        v=queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visit[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visit[i] = 0


dfs(v)
print()
bfs(v)
