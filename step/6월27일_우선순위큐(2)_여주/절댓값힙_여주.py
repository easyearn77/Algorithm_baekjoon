import sys
import heapq

num = int(sys.stdin.readline())
heap = []

for _ in range(num):
    k = int(sys.stdin.readline())
    if k != 0:
        heapq.heappush(heap, (abs(k), k))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
