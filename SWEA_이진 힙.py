T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = []
    lst = list(map(int, input().split()))
    while True:
        heap.append(lst.pop(0))
        temp = len(heap) - 1
        while True:
            if temp % 2:
                if heap[temp] < heap[temp // 2]:
                    heap[temp], heap[temp // 2] = heap[temp // 2], heap[temp]
                    temp //= 2
                    if not temp:
                        break
                else:
                    break
            else:
                if heap[temp] < heap[temp // 2 - 1]:
                    heap[temp], heap[temp // 2 - 1] = heap[temp // 2 - 1], heap[temp]
                    temp = temp // 2 - 1
                    if not temp:
                        break
                else:
                    break

        if not lst:
            break

    node = len(heap) - 1
    ans = 0
    while True:
        if node % 2:
            node //= 2
            ans += heap[node]
            if not node:
                break
        else:
            node = node // 2 - 1
            ans += heap[node]
            if not node:
                break

    print(f'#{tc} {ans}')