n = int(input())
queue = [] #큐는 deque()사용하는게 편함 (시간 복잡도) // queue=deque([]) <전 문제랑 동일하게 import해 줘야함>
count = 0

for i in range(n):
  order = input().strip() #order=input().split()
  if order.split()[0] == 'push': #if order[0]=='push'
    queue.append(int(order.split()[1])) #queue.append(order[1])
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
