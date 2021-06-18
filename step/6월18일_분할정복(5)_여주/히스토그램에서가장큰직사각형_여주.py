from collections import deque

while 1:
  his = list(map(int, input().split()))
  n = his.pop(0)

  if n == 0:
    break
  
  stack = deque()
  ans = 0

  for i in range(n):
    while len(stack) != 0 and his[stack[-1]] > his[i]:
      tmp = stack.pop()

      if len(stack) == 0:
        width = i
      else:
        width = i - stack[-1] - 1
      ans = max(ans, width * his[tmp])
    stack.append(i)
  
  while len(stack) != 0:
    tmp = stack.pop()

    if len(stack) == 0:
      width = n
    else:
      width = n - stack[-1] - 1
    ans = max(ans, width * his[tmp])
  
  print(ans)
