import sys
input = sys.stdin.readline

def f(n):
    while n:
        if n % 10 != 4 and n % 10 != 7:
            return False
        n //= 10
    return True
n = int(input())
for i in range(1, n + 1):
    if n % i == 0 and f(i):
        print("YES")
        exit(0)
print("NO")