#이 문제도 저번 토마토 문제와 동일하다고 판단. 대신 2차원에서 3차원으로 변경됨.
#따라서 bfs로 풀 것임.

import sys
from collections import deque

box=[]
queue=deque()

dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]

m,n,h=map(int,sys.stdin.readline().split()) #box의 크기 입력
for i in range(h):
    box.append([])
    for j in range(n):
        box[i].append(list(map(int,sys.stdin.readline().split()))) #토마토 상태 입력
        for k in range(m):
            if box[i][j][k]==1:
                queue.append([i,j,k]) #초기 정점 queue에 저장

def bfs():
    while queue:
        z,y,x=queue.popleft()
        for i in range(6):
            nz=z+dz[i]
            ny=y+dy[i]
            nx=x+dx[i]

            if 0<=nz<h and 0<=ny<n and 0<=nx<m and box[nz][ny][nx]==0:
                queue.append([nz,ny,nx])
                box[nz][ny][nx]=box[z][y][x]+1

bfs()
answer=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k]==0:
                print(-1)
                exit(0)
            answer=max(answer,box[i][j][k])

print(answer-1)
