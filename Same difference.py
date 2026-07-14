import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    target = s[-1]
    ans = 0
    for i in range(n - 1):
        if s[i] != target:
            ans += 1
    print(ans)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
