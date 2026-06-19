import sys
input = sys.stdin.readline

MOD = int(1e9 + 7)
n = int(input())
ans, p = 1, 1
for x in range(1, n + 1):
    if x < n:
        p = p * 2 % MOD
    ans = ans * x % MOD
print(((ans - p) % MOD + MOD) % MOD)