from collections import deque

bit = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4,
       (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8, (3, 1, 1, 2): 9}
alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def bin(n):
    if n in alpha:
        n = alpha[n]
    else:
        n = int(n)

    temp = []
    while True:
        if n == 0:
            break
        if n == 1:
            temp.append('1')
            break
        elif n % 2:
            temp.append('1')
            n //= 2
        else:
            temp.append('0')
            n //= 2
    s = ''
    for _ in range(4 - len(temp)):
        s += '0'
    while temp:
        s += temp.pop()
    return s

def decode(i, j):
    orgcode = ''
    cnt = 0
    while True:
        temp = video[i][j - cnt]
        if temp == '0':
            break
        else:
            orgcode = bin(temp) + orgcode
            cnt += 1
    multi = len(orgcode) // 56
    # 끝자리가 1이 되도록 정제
    while orgcode[-1] == '0':
        orgcode = '0' + orgcode[:-1]
    while len(orgcode) % 56:
        orgcode = orgcode[1:]
    print(orgcode)
    # 56자로 축약
    comcode = ''
    for part in range(0, 56, multi):
        comcode += orgcode[part]
    print(comcode)
    # 축약된 코드 해석
    cnt = 1
    code = []
    for k in range(56):
        if comcode[-1 - k] == comcode[-1 - k + 1]:
            cnt += 1
        else:
            code.insert(0, cnt)
            cnt = 1
    if cnt:
        code.insert(0, cnt)

    odd = even = total = 0
    for n in range(8):
        temp = tuple(code[(n * 4):(n * 4 + 4)])
        if n == 7:
            keynum = bit[temp]
        elif n % 2:
            even += bit[temp]
        else:
            odd += bit[temp]
        total += bit[temp]

    if (odd * 3 + even + keynum) % 10:
        return 0
    else:
        return total

T = int(input())
for tc in range(1, T + 1):
    ans = 0
    N, M = map(int, input().split())
    video = [list(input()) for _ in range(N)]
    skip = False
    for i in range(N):
        if video[i] == [0] * M:
            skip = False
        if skip:
            continue
        for j in range(M - 1, -1, -1):
            if video[i][j] != '0':
                ans += decode(i, j)
                skip = True
                break

    print(f'#{tc} {ans}')