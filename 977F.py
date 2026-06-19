import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = a
b = list(set(sorted(b)))

def find(x):
    l, r = 0, len(b) - 1
    while l < r:
        md = (l + r) // 2
        if b[md + 1] <= x:
            l = md + 1
        else:
            r = md
    return l
for i in range(n):
    a[i] = find(a[i])
dp = [0] * int(2e5)
ans, idx = 0, 0
for i in range(n):
    dp[a[i]] = 1
    if a[i] > 0:
        if b[a[i]] == b[a[i] - 1] + 1:
            dp[a[i]] = dp[a[i] - 1] + 1
    if dp[a[i]] > ans:
        ans = dp[a[i]]
        idx = i
print(ans)
ar = [idx]
for i in range(idx - 1, -1, -1):
    if b[a[i]] == b[a[idx]] - 1:
        idx = i
        ar.append(idx)
ar = list(reversed(ar))
for i in range(ans):
    print(ar[i] + 1, end = " ")