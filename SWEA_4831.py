T = int(input())

for i in range(T):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    elec = K
    now = 0
    charge = 0
    dis = []
    for j in range(1, len(stops)):
        dis.append(stops[j] - stops[j - 1])
    if max(dis) > K:
        charge = 0
    else:
        while now < N:
            if elec > 0:
                elec -= 1
                now += 1
            elif elec == 0 and now in stops:
                elec = K
                charge += 1
            else:
                while True:
                    elec += 1
                    now -= 1
                    if now in stops:
                        elec = K
                        charge += 1
                        break
                    else:
                        continue

    print(f'#{i + 1} {charge}')