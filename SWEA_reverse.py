T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    lst = []
    for j in range(n):
        lst.append(input())

    for j in range(n):
        for k in range(n-m+1):
            word = lst[j][k:k+m]
            rev = ''.join(reversed(word))
            if word == rev:
                ans = word

    for j in range(n):
        for k in range(n-m+1):
            word = ''
            for l in range(m):
                word += lst[k+l][j]
            rev = ''.join(reversed(word))
            if word == rev:
                ans = word

    print(f'#{i+1} {ans}')