import sys
input = sys.stdin.readline

MOD = int(1e9 + 7)
dp = [0] * int(2e5 + 10)
count = [0] * 10
for _ in range(10):
    dp[_] = 1
count[9] = 1
for i in range(10, int(2e5 + 10)):
    x = count[9]
    for j in range(9, 0, -1):
        count[j] = count[j - 1]
    count[0] = x
    count[1] += x
    count[1] %= MOD
    for j in range(10):
        dp[i] += count[j]
        dp[i] %= MOD
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = 0
    while n > 0:
        ans += dp[n % 10 + m]
        n //= 10
    print(ans % MOD)
