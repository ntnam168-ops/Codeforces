import sys, math
input = sys.stdin.readline

n, m =  map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    ans = math.gcd(ans, abs(a[i] - a[i + 1]))
for i in range(m):
    print(math.gcd(ans, a[0] + b[i]), end = ' ')