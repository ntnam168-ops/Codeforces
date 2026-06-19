import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mp = [0] * (n + 1)
    count = 0
    for x in a:
        mp[x] += 1
    for i in range(n):
        s = a[i]
        for j in range(i + 1, n):
            s += a[j]
            if s > n:
                break
            count += mp[s]
            mp[s] = 0
    print(count)