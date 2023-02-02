T = int(input())

for k in range(T):
    N = int(input())
    nlist = list(map(int, input().split()))
    drop = []
    for i in range(N):
        count = 0
        for j in nlist[i + 1:]:
            if j < nlist[i]:
                count += 1
        drop.append(count)

    print(f'#{k + 1} {max(drop)}')