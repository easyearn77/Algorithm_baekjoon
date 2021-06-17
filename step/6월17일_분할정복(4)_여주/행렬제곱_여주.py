n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def pow_arr(a, b):
  if b == 1:
    for i in range(n):
      for j in range(n):
        a[i][j] %= 1000
    return a
  elif b % 2 == 1:
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    c = pow_arr(a, b-1)
    for i in range(n):
      for j in range(n):
        for k in range(n):
          tmp[i][j] += c[i][k] * a[k][j]
        tmp[i][j] %= 1000
    return tmp
  else:
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    c = pow_arr(a, b // 2)
    for i in range(n):
      for j in range(n):
        for k in range(n):
          tmp[i][j] += c[i][k] * c[k][j]
        tmp[i][j] %= 1000
    return tmp

result = pow_arr(a, b)
for q in result:
  for p in q:
    print(p, end=' ')
  print()
