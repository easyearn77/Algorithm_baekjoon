import sys


def power(a, b):
    global p
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


n, k = map(int, sys.stdin.readline().split())
p = 1000000007

fact = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % p

A = fact[n]
B = (fact[n - k] * fact[k]) % p

print((A % p) * (power(B, p - 2) % p) % p)

#
#페르마의 소정리 이용 (너무 어려웠다)
#b^(p-1) 를 p로 나눈 나머지는 1이다. ->>
#(a/b)%p
#=(a*(b^-1))%p
#=(a)*(b^-1)*(b^(p-1))%p
#=(a%p)*(b^(p-2)%p)%p