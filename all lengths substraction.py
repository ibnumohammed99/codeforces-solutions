t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    cover = [0] * n
    ok = True

    for k in range(n, 0, -1):
        start = -1

        for i in range(n):
            if cover[i] < p[i]:
                start = i
                break

        if start == -1:
            start = 0

        if start + k > n:
            ok = False
            break

        for i in range(start, start + k):
            cover[i] += 1

    if ok and cover == p:
        print("YES")
    else:
        print("NO")
