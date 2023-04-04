def dijkstra(n, s):
    for i in adj[n]:
        nxt, d = i
        if distance[nxt] <= s + d:
            continue
        distance[nxt] = s + d
        dijkstra(nxt, s + d)
T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for node in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))
    distance = [1e10] * (N + 1)
    dijkstra(0, 0)
    ans = distance[N]
    print(f'#{tc} {ans}')