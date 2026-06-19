import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
left, right = [0] * n, [0] * n
left[0] = 1
right[n - 1] = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        left[i] = left[i - 1] + 1
    else:
        left[i] = 1
for i in range(n - 2, -1, -1):
    if a[i] < a[i + 1]:
        right[i] = right[i + 1] + 1
    else:
        right[i] = 1
ans = 0
for i in range(n):
    ans = max(ans, max(left[i], right[i]))
    if left[i] < i + 1 or i < n - 1:
        ans = max(ans, left[i] + 1)
    if right[i] < n - i or i > 0:
        ans = max(ans, right[i] + 1)
for i in range(1, n - 1):
    if a[i + 1] - a[i - 1] > 1:
        ans = max(ans, left[i - 1] + right[i + 1] + 1)
    ans = max(ans, max(left[i - 1], right[i + 1]) + 1)
print(ans)