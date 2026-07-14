import sys

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        s = input_data[idx + 1]
        idx += 2
        
        diff = []
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                diff.append(1)
            else:
                diff.append(0)
        blocks = 0
        in_block = False
        for val in diff:
            if val == 1:
                if not in_block:
                    blocks += 1
                    in_block = True
            else:
                in_block = False
        
        if blocks <= 1:
            results.append("Yes")
        else:
            results.append("No")
            
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()
