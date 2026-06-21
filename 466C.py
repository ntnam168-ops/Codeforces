import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    a[i] += a[i - 1]
if a[n - 1] % 3:
    print(0)
    exit(0)
ans, count = 0, 0
for i in range(n - 1):
    x = a[i]
    if x == a[n - 1] / 3 * 2:
        ans += count
    if x == a[n - 1] / 3:
        count += 1
print(ans)