import sys
import heapq

INF = sys.maxsize

n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start):
    heap = []

    dist = [INF] * (n + 1)
    heapq.heappush(heap, [0, start])
    dist[start] = 0

    while heap:
        d, now_n = heapq.heappop(heap)
        if dist[now_n] < d:
            continue
        for new in graph[now_n]:
            sum_d = d + new[1]
            if sum_d < dist[new[0]]:
                dist[new[0]] = sum_d
                heapq.heappush(heap, [sum_d, new[0]])

    return dist


start_dijk = dijkstra(1)

v1_dijk = dijkstra(v1)
v2_dijk = dijkstra(v2)

ans = min(start_dijk[v1] + v1_dijk[v2] + v2_dijk[n], start_dijk[v2] + v2_dijk[v1] + v1_dijk[n])

print(ans) if ans < INF else print(-1)
