import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    val = 0
    for x in a:
        b[x] += 1
        if b[x] > 2:
            val = x
    if val:
        print(val)
    else:
        print(-1)