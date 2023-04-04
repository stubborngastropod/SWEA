import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1e8] * N for _ in range(N)]
    distance[0][0] = 0
    q = [(0, 0)]
    while q:
        y, x = heapq.heappop(q)
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if ny < 0 or ny > N - 1 or nx < 0 or nx > N - 1:
                continue
            fuel = 1
            if lst[ny][nx] > lst[y][x]:
                fuel += lst[ny][nx] - lst[y][x]
            if distance[ny][nx] > distance[y][x] + fuel:
                distance[ny][nx] = distance[y][x] + fuel
                heapq.heappush(q, (ny, nx))
    ans = distance[-1][-1]
    print(f'#{tc} {ans}')