import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        print(i + 1, 3 * n - 2 * i, 3 * n - 2 * i - 1, end = " ")
    print()