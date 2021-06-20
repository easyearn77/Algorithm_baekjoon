import sys


def bin_search(arr, num,start,end):
    if start>end:
        return 0
    mid = (start + end) // 2
    if num == arr[mid]:
        return 1
    elif num > arr[mid]:
        return bin_search(arr, num,mid+1,end)
    else:
        return bin_search(arr, num,start,mid-1)


n = int(sys.stdin.readline())
A = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = map(int, sys.stdin.readline().split())
for i in B:
    print(bin_search(A, i,0,n-1))
