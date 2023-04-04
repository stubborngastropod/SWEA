def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = []
    for node in range(E):
        n1, n2, w = map(int, input().split())
        adj.append((w, n1, n2))
    adj.sort()
    ans = 0
    parent = [i for i in range(V + 1)]
    for e in range(E):
        w, a, b = adj[e]
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            ans += w

    print(f'#{tc} {ans}')