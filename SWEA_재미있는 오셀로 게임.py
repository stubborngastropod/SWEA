dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    # 초기 돌 셋팅
    wy = wx = N//2
    board[wy][wx] = board[wy - 1][wx - 1] = 2
    board[wy - 1][wx] = board[wy][wx - 1] = 1
    # 돌 두기
    for j in range(M):
        x, y, c = map(int, input().split())
        # 좌표 보정
        x -= 1
        y -= 1
        board[y][x] = c
        for delta in range(8):
            # 보드 내 확인
            if y + dy[delta] in range(N) and x + dx[delta] in range(N):
                # 다른색 돌 여부 확인
                if board[y + dy[delta]][x + dx[delta]] == abs(c - 3):
                    cnt = 0
                    # 한 방향으로 진행, 카운트 저장
                    while True:
                        # 다음 돌이 다른색이고 그 다음 넘어갈 칸이 있을 때 카운트++ 진행
                        if board[y + dy[delta]*(cnt+1)][x + dx[delta]*(cnt+1)] == abs(c - 3):
                            cnt += 1
                            if y + dy[delta]*(cnt+1) in range(N) and x + dx[delta]*(cnt+1) in range(N):
                                continue
                            else:
                                cnt = 0
                                break
                        elif board[y + dy[delta]*(cnt+1)][x + dx[delta]*(cnt+1)] == c:
                            break
                        else:
                            cnt = 0
                            break
                    # 카운트만큼 칸 색칠
                    if cnt:
                        for flip in range(cnt):
                            board[y + dy[delta] * (flip + 1)][x + dx[delta] * (flip + 1)] = c

    # 돌 세기
    black = 0
    white = 0
    for yy in range(N):
        for xx in range(N):
            if board[yy][xx] == 1:
                black += 1
            elif board[yy][xx] == 2:
                white += 1

    print(f'#{i} {black} {white}')