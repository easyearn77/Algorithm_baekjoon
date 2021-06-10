n = int(input())
queue = [i+1 for i in range(n)] #from collection import deque 사용하면, 코드가 더 쉬움!

while len(queue) > 1:
  if len(queue) % 2:
    temp = [queue[-1]]
    temp.extend(queue[1::2])
    queue = temp
  else:
    queue = queue[1::2]
  
print(queue[0])
