n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

for i in m_list:
  low, high = 0, n
  while low <= high:
    mid = (low + high) // 2
    if mid < n and mid > -1:
      if n_list[mid] < i:
        low = mid + 1
      else:
        high = mid - 1
    else:
      break
  if mid < n and mid > -1:
    if i == n_list[high + 1]:
      print(1)
    else:
      print(0)
  else:
    print(0)
