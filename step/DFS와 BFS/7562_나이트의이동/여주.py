from collections import deque

dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]
#나이트가 이동할 수 있는 경우는 총 8개

def bfs(a, b, c, d):
    queue = deque()
    queue.append((a, b))

    while queue:
        curX, curY = queue.popleft()
        if curX == c and curY == d:
            print(visited[curX][curY] - 1)
            return True

        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[curX][curY] + 1
                queue.append((nx, ny))

    return False


n = int(input())
for i in range(n):
    l = int(input())
    visited = [[0] * l for _ in range(l)] # 아직 밟지 않은 칸 0으로 초기화
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    visited[a][b] = 1 # 시작점은 이미 밟고 있기 때문에 1로 설정
    bfs(a, b, c, d)
