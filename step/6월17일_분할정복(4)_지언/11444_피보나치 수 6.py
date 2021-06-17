import sys

p = 1000000007
mul = [[1, 1], [1, 0]]


def multiple_matrix(a,b):
    multipled_matrix = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                multipled_matrix[i][j] += a[i][k] * b[k][j]
            multipled_matrix[i][j] %= p
    return multipled_matrix


def squared(adj, r):  # a^r
    if r == 1:
        return adj
    elif r % 2:
        s_matrix = multiple_matrix(squared(adj, r - 1),adj)
        return s_matrix
    else:
        s_matrix = squared(multiple_matrix(adj,adj),r//2)
        return s_matrix

mul=[[1,1],[1,0]]
n=int(sys.stdin.readline())
matrix=squared(mul,n)
print(matrix[0][1])