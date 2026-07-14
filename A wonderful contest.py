import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    if 100 in a:
        print("Yes")
    else:
        print("No")

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
