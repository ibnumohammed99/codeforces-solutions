def solve():
    n, m = map(int, input().split())

    row_a = [1 if j % 4 in (0, 3) else 0 for j in range(m)]
    row_b = [1 - value for value in row_a]

    pattern = [row_a, row_b, row_b, row_a]

    for i in range(n):
        print(*pattern[i % 4])


for _ in range(int(input())):
    solve()
