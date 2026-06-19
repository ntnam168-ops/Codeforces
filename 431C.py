import sys
input = sys.stdin.readline

MOD = int(1e9 + 7)
n, k, d = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n + 1):
    for j in range(0, min(i, k) + 1):
        for l in range(1, min(k, n - i) + 1):
            dp[i + l][max(j, l)] += dp[i][j]
            dp[i + l][max(j, l)] %= MOD
ans = 0
for i in range(d, k + 1):
    ans += dp[n][i]
    ans %= MOD
print(ans)