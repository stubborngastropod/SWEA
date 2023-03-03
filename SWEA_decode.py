from collections import deque

bit = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4,
       (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8, (3, 1, 1, 2): 9}
alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

# 대충 네자리 이진수로 만드는 함수
def bin(lst):
    newstr = ''
    for n in lst:
        if n in alpha:
            n = alpha[n]
        else:
            n = int(n)

        binnum = []
        while True:
            if n == 0:
                break
            if n == 1:
                binnum.append('1')
                break
            elif n % 2:
                binnum.append('1')
                n //= 2
            else:
                binnum.append('0')
                n //= 2
        s = ''
        for _ in range(4 - len(binnum)):
            s += '0'
        while binnum:
            s += binnum.pop()
        newstr += s
    return newstr

# 대충 암호 해독하는 함수
def decode(code, i):
    orgcode = ''
    cnt = 0
    change = 0
    # 1과 0이 바뀌는 횟수가 30회가 될 때까지 1과0을 그대로 받아주기
    while change <= 30:
        now = code[i - cnt]
        if orgcode and now != orgcode[0]:
            change += 1
        orgcode = now + orgcode
        cnt += 1

    # 56의 배수가 되도록 앞부분에 0 계속 붙여주기
    while len(orgcode) % 56:
        orgcode = '0' + orgcode
    # 이진수 총 길이 저장
    global binlen
    binlen = len(orgcode)
    multi = len(orgcode) // 56
    # 56자로 축약
    comcode = ''
    for part in range(0, len(orgcode), multi):
        comcode += orgcode[part]

    # 축약된 암호 해석
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

    # 암호 진위 여부 확인
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
    temp = [0] * M
    codes = []
    # 같은 패턴의 행 중복 제거
    for i in range(N):
        if video[i] != temp:
            skip = False
            temp = video[i]
            codes.append(temp)
        if skip:
            continue
    # 각 행에 걸쳐있는 중복 암호 제거
    for i in range(len(codes)):
        for j in range(len(codes[i])):
            if codes[i][j] == codes[i-1][j]:
                cnt = 0
                while i + cnt in range(len(codes)) and codes[i + cnt][j] == codes[i-1][j]:
                    codes[i + cnt][j] = 0
                    cnt += 1

    binlen = 0
    for code in codes:
        # 이진수로 바꿔주기
        code = bin(code)
        for i in range(len(code) - 1, -1, -1):
            # 만약 찾은 암호가 있다면 해당 암호의 이진수 길이만큼 continue
            if binlen:
                binlen -= 1
                continue
            if code[i] == '1':
                ans += decode(code, i)

    print(f'#{tc} {ans}')