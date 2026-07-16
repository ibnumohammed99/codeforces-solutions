for _ in range(int(input())):
    input()
    seen = set()
    ans = 0

    for ch in input().strip():
        if ch in seen:
            ans += 1
        else:
            seen.add(ch)
            ans += 2

    print(ans)
