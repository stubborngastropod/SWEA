T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    lst = []
    for j in range(N):
        lst.append(list(map(int, input().split())))
    ans = []

    for j in range(N):
        rcnt = ccnt = 0
        for k in range(N):
            if lst[j][k]:
                rcnt += 1
            else:
                ans.append(rcnt)
                rcnt = 0

            if lst[k][j]:
                ccnt += 1
            else:
                ans.append(ccnt)
                ccnt = 0

        ans.append(rcnt)
        ans.append(ccnt)
    print(f'#{i+1} {ans.count(K)}')