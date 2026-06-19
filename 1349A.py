import sys, math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
nt = [0] * int(2e5 + 1)
for i in range(2, int(2e5 + 1)):
    if nt[i] == 0:
        for j in range(i, int(2e5 + 1), i):
            nt[j] = i
count = [[] for _ in range(int(2e5 + 1))]
for x in a:
    while x > 1:
        p = nt[x]
        c = 0
        while x % p == 0:
            x //= p
            c += 1
        count[p].append(c)
ans = 1
for i in range(2, int(2e5 + 1)):
    if len(count[i]) >= n - 1:
        count[i].sort()
        ans *= i ** count[i][len(count[i]) - n + 1]
print(ans)