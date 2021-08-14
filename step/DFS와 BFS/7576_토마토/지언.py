# 이전 문제와 비슷하게, 최단거리를 구하는 문제와 같다.
# 따라서, bfs로 푼다.

import sys
from collections import deque

queue = deque() #bfs이므로 지나갈 정점을 저장할 queue사용
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
box = [] #토마토가 들어갈 박스(칸)

m, n = map(int, sys.stdin.readline().split())
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split())) #박스에 들어갈 토마토 정보 저장
    box.append(tmp)
    if 1 in tmp:
        queue.append([i, tmp.index(1)]) #초기 정점 queue에 저장 // 이렇게 하니까 백준에서 오류남. pycharm은 잘 됨.
    #이렇게 바꿔야 백준에서 통과됨.ㅠㅠ
    '''    for j in range(m):
        if box[i][j]==1:
            queue.append([i,j]) #초기 정점 queue에 저장'''


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1 #nx,ny에 있는 토마토가 익는 최소 날짜 저장
                queue.append([nx, ny]) #정점 추가


bfs()
print(box)
answer = 0
for i in box:
    if 0 in i:
        print(-1)
        exit(0)
    answer = max(answer, max(i))

print(answer - 1)
#여주) 서로 비슷하게 했네ㅋㅋㅋㅋ 화이팅!!!
