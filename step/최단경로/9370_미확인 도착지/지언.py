import sys
from heapq import heappush,heappop

input = sys.stdin.readline
INF=100000000


def dijkstra(start):
    heap = []
    dist = [INF for _ in range(n+1)]
    dist[start]=0
    heappush(heap, [0, start])

    while heap:
        distance, node = heappop(heap)
        for cn in graph[node]:
            i_cn_d = distance + cn[1]
            if dist[cn[0]] > i_cn_d:
                dist[cn[0]] = i_cn_d
                heappush(heap, [i_cn_d, cn[0]])
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    dest = []
    for _ in range(t):
        dest.append(int(input()))

    stoe=dijkstra(s)
    gtoe=dijkstra(g)
    htoe=dijkstra(h)
    answer=[]
    for e in dest:
        if stoe[g] + gtoe[h] + htoe[e] == stoe[e] or stoe[h] + htoe[g] + gtoe[e] ==stoe[e]:
            answer.append(e)
    answer.sort()
    for ans in answer:
        print(ans,end=' ')
    print()






