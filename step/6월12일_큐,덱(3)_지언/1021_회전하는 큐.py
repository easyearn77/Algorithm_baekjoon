from collections import deque

n,m=map(int,input().split())
pick=list(map(int,input().split()))
dq=deque([i+1 for i in range(n)])
answer=0

for i in range(m):
    num=pick[i]
    if dq.index(num) <= (len(dq)-1)/2:
        while dq[0]!=num:
            dq.append(dq.popleft())
            answer+=1
    else:
        while dq[0]!=num:
            dq.appendleft(dq.pop())
            answer+=1
    dq.popleft()

print(answer)