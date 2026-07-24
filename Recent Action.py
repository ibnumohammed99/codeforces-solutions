for _ in range(int(input())):
    n, m = map(int, input().split())
    actions = list(map(int, input().split()))

    seen = set()
    remove_time = []

    for time, post in enumerate(actions, 1):
        if post not in seen:
            seen.add(post)

            if len(remove_time) < n:
                remove_time.append(time)

    answer = [-1] * (n - len(remove_time))
    answer.extend(remove_time[::-1])

    print(*answer)
