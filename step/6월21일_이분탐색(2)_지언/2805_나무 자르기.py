#pypy3로 해결

import sys

n, m = map(int, sys.stdin.readline().split())
length = list(map(int, sys.stdin.readline().split()))

highest=max(length)
start=highest-m
end=highest

while end>=start:
    mid=(start+end)//2
    sum=0
    for l in length:
        if l-mid>0:
            sum+=l-mid
    if sum>=m:
        start=mid+1
    else:
        end=mid-1

print(end)

