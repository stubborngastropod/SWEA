T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n = 1
    while True:
        if 2 ** (n - 1) <= N < 2 ** n:
            break
        n += 1
    # root
    if N - (2 ** (n - 1) - 1) <= 2 ** (n - 2):
        root = N - (2 ** (n - 1) - 1) + 2 ** (n - 2)
    else:
        root = 2 ** (n - 2) + 2 ** (n - 2)
    # half
    if (N - (2 ** (n - 1) - 1)) % 2:
        half = 2 * (N - (2 ** (n - 1) - 1))
    else:
        half = 2 * (N - (2 ** (n - 1) - 1)) - 2
    print(f'#{tc} {root} {half}')