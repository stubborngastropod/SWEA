T = int(input())
for i in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for j in range(N):
        lst[j] = (lst[j], j+1)

    def winner(l):
        if len(l) == 1:
            return l[0]
        elif len(l) == 2:
            if l[0][0] - l[1][0] in [-2, 1]:
                return l[0]
            elif l[0][0] - l[1][0] in [-1, 2]:
                return l[1]
            elif l[0][0] - l[1][0] == 0:
                return l[0]
        else:
            l1winner = winner(l[:(len(l)-1)//2+1])
            l2winner = winner(l[(len(l)-1)//2+1:])
            return winner([l1winner, l2winner])

    print(f'#{i} {winner(lst)[1]}')