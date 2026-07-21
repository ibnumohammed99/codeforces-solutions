from collections import Counter

for _ in range(int(input())):
    n = int(input())

    p1 = input().split()
    p2 = input().split()
    p3 = input().split()

    cnt = Counter(p1 + p2 + p3)

    s1 = s2 = s3 = 0

    for word in p1:
        if cnt[word] == 1:
            s1 += 3
        elif cnt[word] == 2:
            s1 += 1

    for word in p2:
        if cnt[word] == 1:
            s2 += 3
        elif cnt[word] == 2:
            s2 += 1

    for word in p3:
        if cnt[word] == 1:
            s3 += 3
        elif cnt[word] == 2:
            s3 += 1

    print(s1, s2, s3)
