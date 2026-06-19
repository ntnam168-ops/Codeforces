import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    k = 1
    while n > 0:
        x = (n % 10) * k
        if x: 
            a.append(x)
        k *= 10
        n = int(n / 10)
    print(len(a))
    for x in a:
        print(x, end = " ")
    print()