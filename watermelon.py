def solve(w):
    if w > 2 and w % 2 == 0:
        return "YES"
    return "NO"
print(solve(int(input())))
