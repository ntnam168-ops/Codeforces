import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    mp = [0] * (3 * n + 1)
    bf = 1
    mp[1] = 1
    print(1, end = " ")
    for i in range(n - 1):
        x = bf
        while mp[bf]:
            bf += 1
        mp[bf] = 1
        mp[bf + x] = 1
        print(bf, end = " ")
    print()