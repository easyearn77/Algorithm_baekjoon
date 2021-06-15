n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

cnt0 = 0
cnt1 = 0
cnt2 = 0

def sol(x, y, n):
  global cnt0, cnt1, cnt2
  num = paper[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if num != paper[i][j]:
        for k in range(3):
          for l in range(3):
            sol(x+n//3*k, y+n//3*l, n//3)
        return
  if num == -1:
    cnt0 += 1
  elif num == 0:
    cnt1 += 1
  else:
    cnt2 += 1

sol(0, 0, n)
print(cnt0)
print(cnt1)
print(cnt2)
