import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = min(a)
    ans = 0
    for i in range(n):
        ans += a[i] - x
    print(ans)