import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    count = 0
    for i in range(n - 1):
        u, v = map(int, input().split())
        if u == x or v == x:
            count += 1
    if n == 1:
        print("Ayush")
        continue
    if count == 1:
        print("Ayush")
    else:
        if n % 2 == 0:
            print("Ayush")
        else:
            print("Ashish")