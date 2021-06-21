import sys

k, n = map(int, sys.stdin.readline().split())
lengths = [int(sys.stdin.readline()) for _ in range(k)]
start,end=1,max(lengths)

while start<=end:
    mid=(start+end)//2
    lines=0
    for i in lengths:
        lines+=i//mid

    if lines>=n:
        start=mid+1
    else:
        end=mid-1

print(end)