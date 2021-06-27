import heapq
import sys

n = int(sys.stdin.readline())
hq = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(hq, (abs(num), num))
    else:
        try:
            print(heapq.heappop(hq)[1])
        except:
            print(0)
