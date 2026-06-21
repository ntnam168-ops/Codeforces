import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(sorted(a))
if b == a:
    print("yes")
    print(1, 1)
    exit(0)
c = []
for i in range(n):
    if a[i] != b[i]:
        c.append(i)
if c[-1] - c[0] + 1 != len(c):
    if c[-1] - c[0] == len(c):
        for i in range(c[0], c[-1] + 1):
            if b[i] == a[i]:
                c.append(i)
                break
        c = list(sorted(c))
    else:
        print("no")
        exit(0)
for i in range(c[1], c[-1] + 1):
    if a[i] > a[i - 1]:
        print("no")
        exit(0)
print("yes")
print(c[0] + 1, c[-1] + 1)