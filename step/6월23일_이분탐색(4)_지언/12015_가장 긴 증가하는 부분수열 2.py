#pypy3로 해결
import sys

n = int(sys.stdin.readline())
A = list(map(int, input().split()))
dp = [0]

# list A의 값들을 하나씩 임시 부분수열과 비교하여,
# 부분수열을 만들어 나간다.
for i in range(n):
    low = 0
    high = len(dp) - 1
    while low <= high:
        mid = (low + high) // 2
        if dp[mid] < A[i]:
            low = mid + 1
        else:
            high = mid - 1

    if low >= len(dp):  # 임시 부분수열의 최대값보다 A[i]가 크다면,
        dp.append(A[i])
    else:
        dp[low] = A[i]
        # 어처피 dp[low]의 값이 바뀌어도, 부분수열의 길이는 달라지지 않음.
print(len(dp) - 1)  # 초기값으로 넣은 '0'을 뺀 순 부분수열의 길이
