for i in range(10):
    views = 0
    N = int(input())
    bldg = list(map(int, input().split()))
    for j in range(2, len(bldg)-2):
        side = [bldg[j-2], bldg[j-1], bldg[j+1], bldg[j+2]]
        if bldg[j] > max(side):
            views += bldg[j] - max(side)
    print(f'#{i+1} {views}')