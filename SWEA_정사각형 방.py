dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(a, b, c):
    temp = lst[a][b]
    find = False
    for d in range(4):
        if a + dy[d] in range(n) and b + dx[d] in range(n):
            if lst[a + dy[d]][b + dx[d]] == temp + 1:
                return dfs(a + dy[d], b + dx[d], c + 1)
                find = True
    if not find:
        return c


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = []
    ans = (0, 0, 0)
    for i in range(n):
        lst.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            cnt = dfs(i, j, 1)
            if cnt > ans[2]:
                ans = (i, j, cnt)
            elif cnt == ans[2]:
                if lst[i][j] < lst[ans[0]][ans[1]]:
                    ans = (i, j, cnt)
    room = lst[ans[0]][ans[1]]
    move = ans[2]
    print(f'#{tc} {room} {move}')