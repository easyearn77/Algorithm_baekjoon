def remain(a, b):
  if b == 1:
    return a % c
  else:
    temp = remain(a, b // 2)
    if b % 2 == 0:
      return temp * temp % c
    else:
      return temp * temp * a % c

a, b, c = map(int, input().split())
print(remain(a, b))
