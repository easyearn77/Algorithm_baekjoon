import sys

n = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
measured = [[False] * 15001 for _ in range(n)]
measurable = []


def measure(i, left, right):
    new = abs(left - right)
    if new not in measurable:
        measurable.append(new)

    if i == n:
        return

    if measured[i][new] == 0:
        measure(i + 1, left + weights[i], right)
        measure(i + 1, left, right + weights[i])
        measure(i + 1, left, right)
        measured[i][new] = 1


measure(0, 0, 0)

m = int(sys.stdin.readline())
balls = list(map(int, sys.stdin.readline().split()))

for j in range(m):
    if balls[j] in measurable:
        print('Y', end=' ')
    else:
        print('N', end=' ')
