T = int(input())
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for i in range(T):
    N, M = map(int, input().split())
    lst = []
    ans = []
    for j in range(N):
        lst.append(list(map(int, input().split())))
    for j in range(N):
        for k in range(M):
            bls = lst[j][k]
            for l in range(2):
                if j+di[l+2] in range(N):
                    bls += lst[j+di[l+2]][k+dj[l+2]]
                if k+dj[l] in range(M):
                    bls += lst[j+di[l]][k+dj[l]]
            ans.append(bls)
    print(f'#{i+1} {max(ans)}')