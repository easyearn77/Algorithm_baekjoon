t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  p = list(map(int, input().split()))
  p1 = [0 for i in range(n)]
  p1[m] = 1
  count = 0

  while 1:
    if p[0] == max(p):
      count += 1
      if p1[0] == 1:
        print(count)
        break
      else:
        del p[0]
        del p1[0]
    else:
      p.append(p[0])
      del p[0]
      p1.append(p1[0])
      del p1[0]
