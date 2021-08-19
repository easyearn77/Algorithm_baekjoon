#이건 이지이지 했음! bfs활용!
import sys
from collections import deque

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and board[nx][ny]==0:
                queue.append([nx,ny])
                board[nx][ny]=board[x][y]+1
                if nx==ex and ny==ey: #이거 추가했더니, 오류 안남!
                    return board[ex][ey]
    return board[ex][ey]

t=int(sys.stdin.readline())
for _ in range(t):
    l=int(sys.stdin.readline())
    board=[[0]*l for _ in range(l)]
    sx,sy=map(int,sys.stdin.readline().split())
    ex,ey=map(int,sys.stdin.readline().split())
    if sx==ex and sy==ey:
        print(0)
    else:
        queue=deque()
        queue.append([sx,sy])
        print(bfs())


