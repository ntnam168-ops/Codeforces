import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    a, b, c, d = 0, 0, 0, 0
    for i in range(n):
        if i % 2:
            if ar[i] % 2:
                a = 1
            else:
                b = 1
        else:
            if ar[i] % 2:
                c = 1
            else:
                d = 1
    if (a and b) or (c and d):
        print("NO")
    else:
        print("YES")
