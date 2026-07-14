t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    prefix_sum = 0
    ans = []

    for i in range(n):
        prefix_sum += arr[i]
        avg = prefix_sum // (i + 1)

        if ans:
            ans.append(min(ans[-1], avg))
        else:
            ans.append(avg)

    print(*ans)
