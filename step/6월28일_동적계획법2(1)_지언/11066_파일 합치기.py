import sys

t=int(sys.stdin.readline())
for _ in range(t):
    k=int(sys.stdin.readline())
    data=list(map(int,sys.stdin.readline().split()))

    table=[[0]*k for _ in range(k)]
    for i in range(k-1):
        table[i][i+1]=data[i]+data[i+1]
        for j in range(i+2,k):
            table[i][j]=table[i][j-1]+data[j]

    for d in range(2,k):
        for i in range(k-d):
            j=i+d
            minimum=[table[i][t]+table[t+1][j] for t in range(i,j)]
            table[i][j]+=min(minimum)

    print(table[0][k-1])