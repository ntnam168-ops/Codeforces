import sys
input = sys.stdin.readline

n = int(input())   
a = [100, 20, 10, 5, 1]
s = 0
for x in a:
    s += int(n / x)
    n %= x
print(s)