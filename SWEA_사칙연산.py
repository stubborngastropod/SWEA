for tc in range(1, 11):
    N = int(input())
    adj = [[] * (N + 1) for _ in range(N + 1)]
    val = [0] * (N + 1)
    op = [0] * (N + 1)
    for i in range(N):
        lst = list(input().split())
        if len(lst) == 4:
            adj[int(lst[0])].append(int(lst[2]))
            adj[int(lst[0])].append(int(lst[3]))
            op[int(lst[0])] = lst[1]
        else:
            val[int(lst[0])] = int(lst[1])
    def operation(n):
        if val[n]:
            return val[n]
        else:
            a = adj[n][0]
            b = adj[n][1]
            if op[n] == '+':
                return operation(a) + operation(b)
            if op[n] == '-':
                return operation(a) - operation(b)
            if op[n] == '*':
                return operation(a) * operation(b)
            if op[n] == '/':
                return operation(a) / operation(b)
    ans = int(operation(1))
    print(f'#{tc} {ans}')