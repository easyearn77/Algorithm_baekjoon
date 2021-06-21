n, m = map(int, input().split())
h = list(map(int, input().split()))
start, end = 1, max(h)

while start <= end:
  mid = (start + end) // 2
  ans = 0
  for i in h:
    if i >= mid:
      ans += i - mid
  
  if ans >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)
