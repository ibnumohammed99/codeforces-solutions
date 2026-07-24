for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    found = False

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i] == arr[j]:
                cnt += 1

        if cnt >= 2:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")
