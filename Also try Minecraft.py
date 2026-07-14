import sys

# Fast read
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
a = [int(x) for x in data[2:n+2]]

# Precompute damage costs
pre = [0] * n
for i in range(1, n):
    pre[i] = pre[i-1] + max(0, a[i-1] - a[i])

pref = [0] * n
for i in range(n - 2, -1, -1):
    pref[i] = pref[i+1] + max(0, a[i+1] - a[i])

# Answer queries
res = []
idx = n + 2
for _ in range(m):
    s, t = int(data[idx]) - 1, int(data[idx+1]) - 1
    idx += 2
    res.append(str(pre[t] - pre[s] if s < t else pref[t] - pref[s]))

sys.stdout.write("\n".join(res) + "\n")
