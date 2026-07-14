t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    red_sum = a[0] + a[1]
    blue_sum = a[-1]

    i = 2
    j = n - 2

    while blue_sum <= red_sum and i <= j:
        red_sum += a[i]
        blue_sum += a[j]
        i += 1
        j -= 1

    if blue_sum > red_sum and (n - j - 1) < i:
        print("YES")
    else:
        print("NO")
