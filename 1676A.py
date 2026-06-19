import sys
input = sys.stdin.readline

def T(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

t = int(input())
for _ in range(t):
    n = int(input())
    x = n % 1000
    y = n // 1000
    if T(x) == T(y):
        print("YES")
    else:
        print("NO")