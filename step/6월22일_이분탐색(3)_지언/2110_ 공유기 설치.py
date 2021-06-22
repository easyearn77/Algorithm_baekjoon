import sys

n, c = map(int, sys.stdin.readline().split())
x = sorted([int(sys.stdin.readline()) for _ in range(n)])


def router_counter(distance):
    cnt = 1
    cur_x = x[0]
    for i in range(1, n):
        if cur_x + distance <= x[i]:
            cnt += 1
            cur_x = x[i]
    return cnt


start, end = 1, x[-1] - x[0]
while start<=end:
    mid=(start+end)//2

    if router_counter(mid)>=c:
        answer=mid
        start=mid+1
    else:
        end=mid-1

print(answer)