#6
n=int(input())
A=list(map(int,input().split()))
yet=[0]
answer=[-1 for _ in range(n)]
for i in range(1,n):
    while yet and A[i]>A[yet[-1]]:
        answer[yet[-1]]=A[i]
        yet.pop()
    yet.append(i)

for a in answer:
    print(a, end=' ')