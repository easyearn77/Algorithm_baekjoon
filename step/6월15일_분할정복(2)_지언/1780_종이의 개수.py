import sys
def divide(x,y,l):
    global cnt_0,cnt_m1,cnt_p1
    num=paper[y][x]
    for i in range(y,y+l):
        for j in range(x,x+l):
            if num!=paper[i][j]:
                for a in range(0,l//3*3,l//3):
                    for b in range(0,l//3*3,l//3):
                        divide(x+b,y+a,l//3)
                return
    if num==-1:
        cnt_m1+=1
    elif num==0:
        cnt_0+=1
    elif num==1:
        cnt_p1+=1
    return
n=int(input())
paper=[]
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

cnt_m1=0
cnt_p1=0
cnt_0=0

divide(0,0,n)

print(cnt_m1)
print(cnt_0)
print(cnt_p1)
