import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for x in a:
    if x > 0 and x >= a[k-1]:
        ans += 1
print(ans)