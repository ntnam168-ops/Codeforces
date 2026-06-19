import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n - (k - 1) > 0 and (n - (k - 1)) % 2 == 1:
        print("YES")
        for i in range(k - 1):
            print(1, end = " ")
        print(n - (k - 1))
    elif (n - 2 * (k - 1)) > 0 and (n - (k - 1) * 2) % 2 == 0:
        print("YES")
        for i in range(k - 1):
            print(2, end = " ")
        print(n - (k - 1) * 2)
    else:
        print("NO")