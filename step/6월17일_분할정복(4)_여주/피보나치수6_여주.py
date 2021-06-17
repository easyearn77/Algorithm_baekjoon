c = 1000000007

def mul(a, b):
  ans = []
  for i in range(len(a)):
    ans.append([])
    for j in range(len(b[0])):
      temp = 0
      for k in range(len(a[0])):
        temp += a[i][k] * b[k][j]
      ans[i].append(temp % c)
  return ans

def pow(a, p):
  if p == 1:
    return a
  else:
    temp = pow(a, p // 2)
    if p % 2 == 0:
      return mul(temp, temp)
    else:
      return mul(mul(temp, temp), a)

n = int(input())
m = [[1, 1], [1, 0]]
print(pow(m, n)[0][1])
