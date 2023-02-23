from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pool = [list(input()) for _ in range(N)]
    visited = [[1e4] * M for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                visited[i][j] = 0
                queue.append((i, j))


    def bfs():
        while queue:
            q = queue.popleft()
            a, b = q[0], q[1]
            for d in range(4):
                y = q[0] + dy[d]
                x = q[1] + dx[d]
                if 0 <= y < N and 0 <= x < M and visited[y][x] == 1e4:
                    visited[y][x] = visited[a][b] + 1
                    queue.append((y, x))


    bfs()
    ans = 0
    for i in range(N):
        for j in range(M):
            ans += visited[i][j]

    print(f'#{tc} {ans}')