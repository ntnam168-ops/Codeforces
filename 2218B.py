import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    print(-sum(a) + a[6] * 2)