from collections import deque
import sys

t=int(input())
for _ in range(t):
    p=sys.stdin.readline()
    n=int(input())
    n_list=deque(sys.stdin.readline()[1:-2].split(','))

    if p.count('D') > n:
        print('error')
        continue

    reverse=False
    for order in p:
        if order=='R':
            reverse=not reverse
        elif order=='D':
            if reverse:
                n_list.pop()
            else:
                n_list.popleft()
    if reverse:
        print('[' + ','.join(reversed(n_list))+']')
    else:
        print('[' + ','.join(n_list) + ']')