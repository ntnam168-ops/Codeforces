import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

u = [0] * (int(1e7 + 1))
for i in range(2, int(1e7 + 1)):
    if u[i] == 0:
        for j in range(i, int(1e7 + 1), i):
            u[j] = i

n = int(input())
a, b = [1] * n, [1] * n
aa = list(map(int, input().split()))
for i in range(n):
    ar = []
    x = aa[i]
    while x > 1:
        ar.append(u[x])
        x //= u[x]
    if max(ar) == min(ar):
        a[i] = -1
        b[i] = -1
        continue
    for v in ar:
        if v == ar[len(ar) - 1]:
            a[i] *= v
        else:
            b[i] *= v

for x in a:
    print(x, end=' ')
print()
for x in b:
    print(x, end=' ')