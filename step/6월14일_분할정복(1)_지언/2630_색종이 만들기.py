import sys
def divide(x,y,l):
    global blue,white
    color=sq[y][x]
    for i in range(x,x+l):
        for j in range(y,y+l):
            if sq[j][i]!=color:
                divide(x,y,l//2)
                divide(x+l//2,y,l//2)
                divide(x,y+l//2,l//2)
                divide(x+l//2,y+l//2,l//2)
                return
    if color==1:
        blue+=1
    else:
        white+=1
    return

n=int(input())
sq=[]
for _ in range(n):
    sq.append(list(map(int,sys.stdin.readline().split())))

tmp=n
blue=0
white=0

divide(0,0,n)
print(white)
print(blue)
