T = int(input())
for i in range(T):
    N = int(input())
    table1 = []
    table2 = []
    cnt = 0

    for j in range(10):
        table1.append([0] * 10)
        table2.append([0] * 10)
    for j in range(N):
        *a, b = map(int, input().split())
        if b == 1:
            for k in range(a[0], a[2]+1):
                for l in range(a[1], a[3]+1):
                    table1[k][l] = 1
        if b == 2:
            for k in range(a[0], a[2]+1):
                for l in range(a[1], a[3]+1):
                    table2[k][l] = 1

    for j in range(10):
        for k in range(10):
            if table1[j][k] == table2[j][k] == 1:
                cnt += 1

    print(f'#{i+1} {cnt}')