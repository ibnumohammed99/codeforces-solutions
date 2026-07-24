t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if "..." in s:
        print(2)
    else:
        ans = 0
        for ch in s:
            if ch == '.':
                ans += 1
        print(ans)
