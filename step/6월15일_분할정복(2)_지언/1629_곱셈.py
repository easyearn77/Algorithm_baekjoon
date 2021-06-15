import sys
def power(a,b):
    if b==1:
        return a%c
    else:
        tmp=power(a,b//2) #이게 핵심! (a^2n=(a^n)^2)
        if b%2==0:
            return (tmp**2)%c
        else:
            return tmp**2*a%c
a,b,c=map(int,sys.stdin.readline().split())
print(power(a,b))