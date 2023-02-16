T = int(input())
for i in range(T):
    N = int(input())
    lst = []
    for j in range(N):
        lst.append(list(map(int, input().split())))
    ans = 1e10

    def makesum(n, s, v):
        global ans
        temp = v + [n]
        if len(temp) == N and s < ans:
            ans = s
        else:
            for j in range(N):
                if j not in temp and s + lst[len(temp)][j] < ans:
                    makesum(j, s + lst[len(temp)][j], temp)
    for k in range(N):
        makesum(k, lst[0][k], [])
    print(f'#{i+1} {ans}')