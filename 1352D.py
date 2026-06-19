import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count, x, y = 1, 0, 0
    l, r, last = 0, n - 1, 0
    l += 1
    last = a[0]
    x += a[0]
    while l <= r:
        now = 0
        while now <= last and r >= l:
            now += a[r]
            r -= 1
        if now > last:
            y += now
            count += 1
            last = now
        else:
            if now:
                y += now
                count += 1
            break
        now = 0
        while now <= last and r >= l:
            now += a[l]
            l += 1
        if now > last:
            x += now
            count += 1
            last = now
        else:
            if now:
                x += now
                count += 1
            break
    print(count, x, y)