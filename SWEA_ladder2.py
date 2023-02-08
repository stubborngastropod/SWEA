for i in range(10):
    n = int(input())
    ladder = []
    for j in range(100):
        ladder.append(list(map(int, input().split())))

    def side(x, y, k, cnt):
        if y + k in range(100) and ladder[x][y + k]:
            return side(x, y + k, k, cnt + 1)
        else:
            return y, cnt

    def counting(n):
        cnt = 0
        x, y = 0, n
        while True:
            if y + 1 in range(100) and ladder[x][y + 1]:
                y, cnt = side(x, y, 1, cnt)
                cnt += 1
                x += 1
                if x == 99:
                    break
            elif y - 1 in range(100) and ladder[x][y - 1]:
                y, cnt = side(x, y, -1, cnt)
                cnt += 1
                x += 1
                if x == 99:
                    break
            else:
                cnt += 1
                x += 1
                if x == 99:
                    break
        return cnt

    mini = 1e10
    ans = 0
    for j in range(100):
        if ladder[0][j] and counting(j) <= mini:
            mini = counting(j)
            ans = j
    print(f'#{i+1} {ans}')
