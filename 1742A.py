import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if max(a, max(b, c)) * 2 == a + b + c:
        print("YES")
    else:
        print("NO")