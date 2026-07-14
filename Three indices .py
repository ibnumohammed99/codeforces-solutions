import sys

input = sys.stdin.read
data = input().split()
t = int(data[0])
idx = 1

for _ in range(t):
    n = int(data[idx])
    p = [int(x) for x in data[idx + 1 : idx + 1 + n]]
    idx += n + 1
    
    found = False
    for i in range(n - 2):
        if p[i] < p[i+1] and p[i+1] > p[i+2]:
            print("YES")
            print(f"{i + 1} {i + 2} {i + 3}")
            found = True
            break
    if not found:
        print("NO")
