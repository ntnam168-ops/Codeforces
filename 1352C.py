import sys
input = sys.stdin.readline


def cal(x, n):
    return x - int(x / n)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l, r = 1, int(1e10)
    while l < r:
        md = int((l + r) / 2)
        if cal(md, n) >= k:
            r = md
        else:
            l = md + 1
    while l % n == 0:
        l -= 1
    print(l)