t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    _ = list(map(int, input().split()))  # unused array
    b = list(map(int, input().split()))

    operations = []

    for level in range(k, 0, -1):
        for i in range(n):
            if b[i] == level:
                while b[i] <= k:
                    operations.append(i + 1)
                    b[i] += 1

    print(len(operations))
    print(*operations)
