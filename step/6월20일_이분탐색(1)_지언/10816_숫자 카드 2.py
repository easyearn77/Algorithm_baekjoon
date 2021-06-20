#이 방법은 정답이 아니었다. 시간초과가 뜬다.
#하지만 이진탐색으로 풀 수 있는 방법이다.
#답은 따로 올려놨다.

import sys

def bin_search(arr,num,start,end):
    if start>end:
        return 0
    mid=(start+end)//2
    if arr[mid]==num:
        return have[start:end+1].count(num)
    elif num<arr[mid]:
        return bin_search(arr,num,start,mid-1)
    else:
        return bin_search(arr,num,mid+1,end)

n=int(sys.stdin.readline())
have=sorted(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
compare=map(int,sys.stdin.readline().split())

answer=[]
for i in compare:
    answer.append(bin_search(have,i,0,n-1))

for j in range(m):
    print(answer[j], end=' ')