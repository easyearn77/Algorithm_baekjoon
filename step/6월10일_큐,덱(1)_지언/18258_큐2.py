import sys
from collections import deque
n=int(sys.stdin.readline())
queue=deque([])
for _ in range(n):
    instruction=sys.stdin.readline().split()
    if instruction[0]=='push':
        queue.append(instruction[1])
    elif instruction[0]=='pop':
        print(queue.popleft()) if queue else print(-1)
    elif instruction[0]=='size':
        print(len(queue))
    elif instruction[0]=='empty':
        print(1) if not queue else print(0)
    elif instruction[0]=='front':
        print(queue[0]) if queue else print(-1)
    elif instruction[0]=='back':
        print(queue[-1]) if queue else print(-1)