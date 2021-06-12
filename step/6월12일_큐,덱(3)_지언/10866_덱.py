from collections import deque
import sys

n=int(sys.stdin.readline())
dq=deque([])

for _ in range(n):
    inst=list(sys.stdin.readline().split())
    if inst[0]=='push_front':
        dq.appendleft(inst[1])
    elif inst[0]=='push_back':
        dq.append(inst[1])
    elif inst[0]=='pop_front':
        print(dq.popleft()) if dq else print(-1)
    elif inst[0]=='pop_back':
        print(dq.pop()) if dq else print(-1)
    elif inst[0]=='size':
        print(len(dq))
    elif inst[0]=='empty':
        print(0) if dq else print(1)
    elif inst[0]=='front':
        print(dq[0]) if dq else print(-1)
    elif inst[0]=='back':
        print(dq[-1]) if dq else print(-1)
