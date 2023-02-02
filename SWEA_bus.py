T = int(input())
for i in range(T):
    N = int(input())

    bus_list = []
    for j in range(N):
        bus = list(map(int, input().split()))
        bus_list.append(bus)

    start, end = bus_list[0][0], bus_list[0][1]
    for j in bus_list:
        if j[0] < start:
            start = j[0]
        if j[1] > end:
            end = j[1]

    stops = [0] * 5000
    for j in bus_list:
        for k in range(j[0], j[1] + 1):
            stops[k - 1] += 1

    P = int(input())

    print(f'#{i + 1}', end=' ')
    for j in range(P):
        c = int(input())
        print(stops[c - 1], end=' ')
    print()