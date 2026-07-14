import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    output = []
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr + 1])
        ptr += 2
        
        mx = 0
        for i in range(n):
            val = int(input_data[ptr])
            if val > mx:
                mx = val
            ptr += 1
            
        case_results = []
        for _ in range(m):
            op = input_data[ptr]
            l = int(input_data[ptr + 1])
            r = int(input_data[ptr + 2])
            ptr += 3
            
            if l <= mx <= r:
                if op == '+':
                    mx += 1
                else:
                    mx -= 1
            case_results.append(str(mx))
        output.append(" ".join(case_results))
        
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()
