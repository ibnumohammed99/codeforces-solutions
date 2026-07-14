import sys

def solve():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = input[idx:idx + n]
        idx += n
        
        l, r = 0, n - 1
        ans = 0
        while l < r:
            if a[l] == '0':
                l += 1
            elif a[r] == '1':
                r -= 1
            else:
                ans += 1
                l += 1
                r -= 1
        results.append(str(ans))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()
