import sys

read = sys.stdin.readline
dic = {}
for i in range(int(read())):
    dic[i + 1] = set()

for j in range(int(read())):
    s, e = map(int, read().split())
    dic[s].add(e)
    dic[e].add(s)


def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)


visited = []
dfs(1, dic)
print(len(visited) - 1)
