# heapq모듈은 이진트리 기반의 최소 힙 자료구조를 제공한다.
import heapq
import sys

n=int(sys.stdin.readline())
h=[]

for _ in range(n):
    num=int(sys.stdin.readline())
    if num==0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h))

    else:
        heapq.heappush(h,num)