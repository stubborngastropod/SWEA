for i in range(10):
    d = int(input())
    box = list(map(int, input().split()))
    while d > 0:
        M = box.index(max(box))
        m = box.index(min(box))
        box[M] -= 1
        box[m] += 1
        d -= 1
    M = box.index(max(box))
    m = box.index(min(box))
    print(f'#{i+1} {box[M]-box[m]}')