n = int(input())
queue = []
count = 0

for i in range(n):
  order = input().strip()
  if order.split()[0] == 'push':
    queue.append(int(order.split()[1]))
  elif order.split()[0] == 'pop':
    if len(queue) - count == 0:
      print(-1)
    else:
      print(queue[count])
      count += 1

  elif order.split()[0] == 'size':
    print(len(queue) - count)
  elif order.split()[0] == 'empty':
    if len(queue) - count == 0:        
      print(1)
    else:
      print(0)
  elif order.split()[0] == 'front':
    if len(queue) - count == 0:
      print(-1)
    else:
      print(queue[count])
  elif order.split()[0] == 'back':
    if len(queue) - count == 0:
      print(-1)
    else:
      print(queue[-1])
