import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    ans = list(range(1, n + 1))

    for i in range(n):
        if ans[i] == p[i]:
            if i + 1 < n:
                ans[i], ans[i + 1] = ans[i + 1], ans[i]
            else:
                ans[i], ans[i - 1] = ans[i - 1], ans[i]

    if any(ans[i] == p[i] for i in range(n)):
        print(-1)
    else:
        print(*ans)
