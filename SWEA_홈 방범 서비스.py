dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(a, b, limit):
    global visited
    global house
    visited[a][b] = 1
    queue = [(a, b, 1)]
    while True:
        qpop = queue.pop(0)
        if qpop[2] == limit:
            return
        for d in range(4):
            if qpop[0] + dy[d] in range(N) and qpop[1] + dx[d] in range(N) and not visited[qpop[0] + dy[d]][
                qpop[1] + dx[d]]:
                if city[qpop[0] + dy[d]][qpop[1] + dx[d]]:
                    house += 1
                visited[qpop[0] + dy[d]][qpop[1] + dx[d]] = 1
                queue.append((qpop[0] + dy[d], qpop[1] + dx[d], qpop[2] + 1))
        if not queue:
            return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = []
    for i in range(N):
        city.append(list(map(int, input().split())))
    max_house = 0

    for i in range(N):
        for j in range(N):
            for k in range(1, N + 2):
                visited = [[0] * (N + 1) for _ in range(N + 1)]
                if city[i][j]:
                    house = 1
                else:
                    house = 0
                bfs(i, j, k)
                if k ** 2 + (k - 1) ** 2 <= house * M:
                    if house > max_house:
                        max_house = house

    print(f'#{tc} {max_house}')