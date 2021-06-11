from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    queue=deque(list(map(int,input().split())))
    q_l=deque([0 for _ in range(n)])
    q_l[m]=1
    cnt=0

    while True:
        if queue[0]==max(queue):
            cnt+=1
            if q_l[0]==1:
                print(cnt)
                break
            else:
                queue.popleft()
                q_l.popleft()
        else:
            queue.append(queue.popleft())
            q_l.append(q_l.popleft())


