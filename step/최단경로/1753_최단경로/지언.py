#조금 많이 어렵넹?ㅋㅋ 답지참고...ㅠㅠ
import sys
from heapq import heappush,heappop
INF=sys.maxsize
v,e= map(int,sys.stdin.readline().split())
st_v=int(sys.stdin.readline())
graph=[[] for _ in range(v+1)]
dp=[INF]*(v+1)
heap=[]

def dijkstra(start):
    dp[start]=0
    heappush(heap, [0,start]) #시작점은 0

    while heap:
        weight,node=heappop(heap) #정점. weight=시작점~정점 무게
        for e_end,e_weight in graph[node]: #정점에 연결된 간선의 끝점, 간선의 무게
            new_weight=e_weight+weight #new_weight=정점을 꼭 지나는 간선의 끝점까지의 무게
            if new_weight<dp[e_end]: #그동안 구했던 무게가 더 크다면
                dp[e_end]=new_weight
                heappush(heap,[new_weight,e_end]) #간선의 끝점과 연결된 다른 점들도 다시 비교

for i in range(e):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u].append([v,w])

dijkstra(st_v)
for i in dp[1:]:
    print(i if i != INF else "INF")
