import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print((max(a) - min(a) + 1) // 2)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
