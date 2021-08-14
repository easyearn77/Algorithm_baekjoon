import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []
queue = deque([])

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
    for j in range(m): #익은 토마토를 큐에 저장
        if graph[i][j] == 1:
            queue.append([i,j])
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(): #bfs 문제는 함수로 푸는게 괜츈한덧!
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a <n and 0 <= b < m and graph[a][b] == 0:
                queue.append([a,b])
                graph[a][b] = graph[x][y] + 1

bfs()
answ = 0

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answ = max(answ,max(i))

print(answ-1)
#(지언) 귣귣 내가 한거랑 비슷해서 할 말이 없다리~ ㅋㅋ 화이팅!
