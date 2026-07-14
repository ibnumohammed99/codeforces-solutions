for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    consecutive = 0
    possible = True

    for ch in s:
        if ch == '1':
            consecutive += 1
            if consecutive == k:
                possible = False
                break
        else:
            consecutive = 0

    if not possible:
        print("NO")
        continue

    print("YES")

    ans = [0] * n
    current = 1

    for i, ch in enumerate(s):
        if ch == '1':
            ans[i] = current
            current += 1

    for i, ch in enumerate(s):
        if ch == '0':
            ans[i] = current
            current += 1

    print(*ans) 
