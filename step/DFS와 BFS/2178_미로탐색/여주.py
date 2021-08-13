import sys
from collections import deque

def bfs(x, y): #bfs 사용 (지언: 함수로 분리하는거 좋은 것 같음)
  queue = deque() #양방향 큐 사용
  queue.append((x, y))
  while queue:
    x, y = queue.popleft() #왼쪽에서 값 빼기
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n-1][m-1]

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().strip()))) #strip 사용하여 양 옆 공백 제거 (지언: 오 이렇게 입력받으면 되는군!)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))
