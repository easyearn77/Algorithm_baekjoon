import sys
def divide(x,y,l):
    num=qt[y][x]
    for i in range(x,x+l):
        for j in range(y,y+l):
            if qt[j][i]!=num:
                arr.append('(')
                divide(x,y,l//2)
                divide(x+l//2,y,l//2)
                divide(x,y+l//2,l//2)
                divide(x+l//2,y+l//2,l//2)
                arr.append(')')
                return
    arr.append(num)

n=int(sys.stdin.readline())
qt=[]
for _ in range(n):
    qt.append(str(sys.stdin.readline()))
arr=[]
divide(0,0,n)
for i in arr:
    print(i,end='')