import sys

n, m = map(int, sys.stdin.readline().split())
mem = [0]+list(map(int, sys.stdin.readline().split()))
cost = [0]+list(map(int, sys.stdin.readline().split()))
result=sum(cost)
dp=[[0 for _ in range(result+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,sum(cost)+1):
        if cost[i]<=j:
            dp[i][j]=max(mem[i]+dp[i-1][j-cost[i]],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
        if dp[i][j]>=m:
            result=min(result,j)
print(result)