t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    a = sorted(input())
    b = sorted(input())

    i = 0
    j = 0

    take_a = 0
    take_b = 0

    ans = []

    while i < n and j < m:

        if take_a == k:
            ans.append(b[j])
            j += 1
            take_b += 1
            take_a = 0

        elif take_b == k:
            ans.append(a[i])
            i += 1
            take_a += 1
            take_b = 0

        elif a[i] < b[j]:
            ans.append(a[i])
            i += 1
            take_a += 1
            take_b = 0

        else:
            ans.append(b[j])
            j += 1
            take_b += 1
            take_a = 0

    print("".join(ans))
