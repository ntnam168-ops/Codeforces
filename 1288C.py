import sys
input = sys.stdin.readline

MOD = int(1e9 + 7)
n, m = map(int, input().split())
gt = [1] * (n + m + 1)
for i in range(1, n + m + 1):
    gt[i] = (gt[i - 1] * i) % MOD
def pow(a, b):
    if b == 1:
        return a
    x = pow(a, b // 2)
    x = (x * x) % MOD
    if b % 2:
        x = (x * a) % MOD
    return x
def C(a, b):
    return gt[b] * pow((gt[a] * gt[b - a]) % MOD, MOD - 2) % MOD
def f(x, m):
    x += m
    return C(m, x - 1)
ans = 0
for i in range(1, n + 1):
    ans = (ans + f(i, m - 1) * f(n - i + 1, m)) % MOD
print(ans)