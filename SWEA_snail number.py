T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(T):
    cnt = 1
    n = int(input())
    snail = [[0] * (n + 2) for j in range(n + 2)]
    for j in range(n + 2):
        snail[0][j] = 1
        snail[j][0] = 1
        snail[n+1][j] = 1
        snail[j][n+1] = 1
    k = j = 1
    x = y = 0
    while cnt < n**2 + 1:
        if snail[k][j] == 0:
            snail[k][j] = cnt
            cnt += 1
        else:
            k -= di[x]
            j -= dj[y]
            x = (x + 1) % 4
            y = (y + 1) % 4
        k += di[x]
        j += dj[y]
    print('#'+str(i+1))
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            print(snail[j][k], end = ' ')
        print()