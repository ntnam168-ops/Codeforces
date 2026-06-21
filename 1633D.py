import sys
input = sys.stdin.readline

t = int(input())
dp = [int(1e5)] * int(1e3 + 1)
dp[1] = 0
for i in range(1, int(1e3 + 1)):
    for j in range(1, i + 1):
        d = i + i // j
        if d > int(1e3):
            continue
        dp[d] = min(dp[d], dp[i] + 1)
for _ in range(t):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    s = 0
    for x in b:
        s += dp[x]
    if k >= s:
        print(sum(c))
        continue
    dp1 = [0] * (k + 1)
    for i in range(n):
        for j in range(k, dp[b[i]] - 1, -1):
            dp1[j] = max(dp1[j], dp1[j - dp[b[i]]] + c[i])
    print(max(dp1))