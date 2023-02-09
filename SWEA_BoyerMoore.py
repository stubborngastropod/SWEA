T = int(input())
for i in range(T):
    a, b = map(str, input().split())

    # skip array 생성
    skiparr = {}
    for j in range(len(b)):
        skiparr[b[j]] = len(b) - 1 - j

    # 반복문 초기 설정
    breaker = True
    x, y = 0, len(b)
    inputcnt = 0

    # 연산
    while breaker:
        temp = a[x:y]

        # 완전히 같을 때 이동
        if temp == b:
            inputcnt += 1
            x += len(b)
            y += len(b)
            if y > len(a):
                breaker = False

        # 완전히 같지 않을 때
        else:
            cnt = 0
            for j in range(len(b)):
                # 다른 부분이 b에 있는 경우 - cnt만큼 temp 이동
                if temp[len(b) - 1 - j] in b:
                    if temp[len(b) - 1 - j] == b[len(b) - 1 - j]:
                        cnt += 1
                    else:
                        x += skiparr[temp[-1 - cnt]]
                        y += skiparr[temp[-1 - cnt]]
                        if y > len(a):
                            breaker = False
                        inputcnt += skiparr[temp[-1 - cnt]]
                        break
                # 다른 부분이 b에 없는 경우 - 전체 이동
                else:
                    x += len(b)
                    y += len(b)
                    if y > len(a):
                        breaker = False
                    inputcnt += len(b)
                    break

    inputcnt += len(b) - (y - len(a))
    print(f'#{i + 1} {inputcnt}')