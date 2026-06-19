import sys
input = sys.stdin.readline
 
def f(a, b):
    if a == b:
        return
    if b - a == 6: 
        print(a + 1, a + 4, a + 2, a + 5, a + 3, a + 6, end = "")
    elif b - a == 7:
        print(a + 1, a + 4, a + 7, a + 5, a + 2, a + 6, a + 3, end = "")
    elif b - a == 8:
        print(a + 1, a + 5, a + 8, a + 4, a + 7, a + 3, a + 6, a + 2, end = "")
    elif b - a == 9:
        print(a + 1, a + 5, a + 9, a + 7, a + 3, a + 6, a + 8, a + 4, a + 2, end = "")

t = int(input())
for _ in range(t):
    n = int(input())
    if n < 4:
        print(-1)
        continue
    if n == 4:
        print(2, 4, 1 , 3)
        continue
    k = 0
    if n % 5:
        k += (5 + n % 5)
    for i in range(int((n - k) / 5)):
        print(i * 5 + 1, i * 5 + 4, i * 5 + 2, i * 5 + 5, i * 5 + 3, end = " ")
    if k:
        f(n - k, n)
    print()