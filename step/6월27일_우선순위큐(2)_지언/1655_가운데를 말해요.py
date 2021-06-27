import heapq
import sys

# 중앙을 기준으로, 더 작은 수는 small에, 더 큰 수는 big에 저장한다.
small, big = [], []
n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    # small 리스트는 최대힙으로 만들고, big 리스트는 최소힙으로 만든다.
    if len(small) == len(big):
        heapq.heappush(small, (-num, num))
    else:
        heapq.heappush(big, (num, num))

    # 만약 small의 최대값이 big의 최소값보다 클 경우.
    if big and small[0][1] > big[0][1]:
        small_change = heapq.heappop(small)[1]
        big_change = heapq.heappop(big)[1]

        heapq.heappush(small, (-big_change,big_change))
        heapq.heappush(big, (small_change,small_change))

    # 작은 수 중 가장 큰 수를 (짝수고려) 출력한다.
    print(small[0][1])
