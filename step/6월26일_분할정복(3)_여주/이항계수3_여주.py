def power(a, b):
  if b == 0:
    return 1
  if  b % 2:
    return (power(a, b // 2) ** 2 * a) % m
  else:
    return (power(a, b //2) ** 2) % m

m = 1000000007
n, k = map(int, input().split())

factorial = [1 for _ in range(n + 1)]

for i in range(2, n+1):
  factorial[i] = factorial[i - 1] * i % m

a = factorial[n]
b = (factorial[n - k] * factorial[k]) % m

print((a % m) * (power(b, m - 2) % m) % m)
