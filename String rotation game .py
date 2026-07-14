t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    transitions = 0
    has_equal_edge = False

    for i in range(n):
        if s[i] != s[(i + 1) % n]:
            transitions += 1
        else:
            has_equal_edge = True

    if has_equal_edge:
        print(transitions + 1)
    else:
        print(transitions)
