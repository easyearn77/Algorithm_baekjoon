#6
import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1 for _ in range(n)]

stack.append(0)
for i in range(1, n):
  while stack and num_list[stack[-1]] < num_list[i]:
    ans[stack.pop()] = num_list[i]
  stack.append(i)

print(*ans)
