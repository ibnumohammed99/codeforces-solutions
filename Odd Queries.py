import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # prefix sum
    pref = [0] * (n + 1)

    for i in range(n):
        pref[i + 1] = pref[i] + a[i]

    total_sum = pref[n]

    for _ in range(q):
        l, r, k = map(int, input().split())

        range_sum = pref[r] - pref[l - 1]
        length = r - l + 1

        new_sum = total_sum - range_sum + (k * length)

        if new_sum % 2 == 1:
            print("YES", end=" ")
        else:
            print("NO", end=" ")

    print()
