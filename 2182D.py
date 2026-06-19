import sys
input = sys.stdin.readline

MOD = 998244353
t = int(input())
gt = [1]
for i in range(1, 51):
    gt.append((gt[i - 1] * i) % MOD)

def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a    
    x = pow(a, b // 2)
    x = x * x % MOD
    if b % 2:
        x = x * a % MOD
    return x

def C(a, b):
    return gt[b] * pow(((gt[a] * gt[b - a]) % MOD), MOD - 2) % MOD 

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    x = min(a[1 : n + 1])
    for i in range(1, n + 1):
        a[i] -= x
    while True:
        count, mn = 0, int(1e6)
        for i in range(1, n + 1):
            if a[i] == 0:
                count += 1
            else:
                mn = min(mn, a[i])
        if count == n:
            break
        d = min(mn, a[0] // count)
        if d == 0:
            break
        for i in range(1, n + 1):
            if a[i]:
                a[i] -= d
        a[0] -= d * count
    if max(a[1 : n + 1]) == 0:
        print(gt[n])
    elif max(a[1 : n + 1]) > 1:
        print(0)
    else:
        s = sum(a[1 : n + 1])
        ans = C(s, s + a[0]) * gt[n - s] * gt[s]
        print(ans % MOD)