from collections import Counter

for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))

    cnt = Counter(arr)

    ans = []

    # First occurrence of every distinct number
    for x in sorted(cnt):
        ans.append(x)

    # Remaining duplicates
    for x in sorted(cnt):
        ans.extend([x] * (cnt[x] - 1))

    print(*ans)
