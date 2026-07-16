for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    s = set()
    i = len(a) - 1
    while i >= 0 and a[i] not in s:
        s.add(a[i])
        i -= 1
    print(i + 1)
