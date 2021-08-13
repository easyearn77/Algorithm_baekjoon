"""
dfs를 사용하는 경우:
    1. 한가지 정점과 연결된 모든 정점을 탐색해야 하는 경우 (한 정점씩 방문 후 재귀)
    2. 경로를 찾아야 되는 경우 (방문하면서 인접요소 확인)
    3. 사이클이 존재하는 경로를 찾는 경우

bfs를 사용하는 경우:
    1. 최단거리를 구해야 하는 경우 (queue를 사용하여 정점 탐색)
    2. 최단겨리를 구하되 조건이 여러개 존재하는 경우
"""
#여듀) 위에처럼 bfs나 dfs 언제 쓰는지 명시해두는거 좋다!

import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline()))

board[0][0] = 1 #문자열로 입력받기 때문에 첫 정점만 숫자로 설정 (여쥬) 첫 정점만 따로 설정하는거 귯귯)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = [[0, 0]] #최단거리-bfs-queue사용

while queue:
    x, y = queue[0][0], queue[0][1] #정점

    del queue[0]

    for i in range(4):
        nx = x + dx[i] #정점 주변 탐색
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if board[nx][ny] == '1':
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1

print(board[n - 1][m - 1])
