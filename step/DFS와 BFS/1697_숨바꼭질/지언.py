#최단거리와 비슷한 문제이므로 bfs를 사용한다.

import sys
from collections import deque
MAX=100001 #max 설정 안하면 오류남. (여주) 문제에서 직선 거리 최대가 100000이라고 주어져서 max를 100001로 설정해야 하나봐!)

n,k=map(int,sys.stdin.readline().split())
road=[0 for _ in range(MAX)]
queue=deque()

#초기 정점
queue.append(n)
road[n]=1

def bfs():
    while queue:
        x=queue.popleft()
        nx=[x-1,x+1,2*x]
        for i in range(3):
            tmp=nx[i]
            if 0<=tmp<MAX and road[tmp]==0:
                road[tmp]=road[x]+1
                queue.append(tmp)
                if tmp==k: #시간 단축을 위한 조건문
                    return

bfs()
print(road[k]-1)
