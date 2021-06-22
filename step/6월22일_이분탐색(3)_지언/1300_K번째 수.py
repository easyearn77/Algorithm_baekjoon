import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
start, end = 1, k

while end >= start:
    mid = (start + end) // 2

    tmp = 0
    for i in range(1, n + 1):
        tmp += min(mid // i, n)
        #i행에서 mid보다 작은 숫자의 갯수를 tmp에 더함

    if tmp >= k: #mid가 k번쩨 숫자(B[k])보다 같거나 크다면,
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
