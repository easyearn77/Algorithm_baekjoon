import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  dp[i][i] = 1
  if i < n-1 and num[i] == num[i+1]:
    dp[i][i+1] = 1

for i in range(1, n):
  for j in range(1, i+1):
    if num[i] == num[i-j] and dp[i-j+1][i-1] == 1:
      dp[i-j][i] = 1

m = int(input())
for _ in range(m):
  s, e = map(int, sys.stdin.readline().split())
  print(dp[s-1][e-1])
