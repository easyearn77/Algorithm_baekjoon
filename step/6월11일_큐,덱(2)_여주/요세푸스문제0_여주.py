from collections import deque
n, k = map(int, input().split())
yose = deque([])

for i in range(1, n+1):
  yose.append(i)
print('<', end = "")

while yose:
  for i in range(k-1):
    yose.append(yose[0])
    yose.popleft()
  print(yose.popleft(), end = "")
  if yose:
    print(', ', end = "")

print('>')
