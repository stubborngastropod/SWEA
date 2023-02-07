for i in range(10):
    n = int(input())
    lst = []
    for j in range(100):
        lst.append(list(map(int, input().split())))
    end = lst[99].index(2)

    def side(x, y, k):
        if y+k not in range(100) or lst[x][y+k] == 0:
            return y
        else:
            return side(x, y+k, k)

    x, y = 99, end
    while True:
        if y - 1 in range(100) and lst[x][y-1]:
            y = side(x, y, -1)
            x -= 1
            if x == 0:
                print(f'#{n} {y}')
                break
            continue
        elif y + 1 in range(100) and lst[x][y+1]:
            y = side(x, y, 1)
            x -= 1
            if x == 0:
                print(f'#{n} {y}')
                break
            continue
        else:
            x -= 1
            if x == 0:
                print(f'#{n} {y}')
                break