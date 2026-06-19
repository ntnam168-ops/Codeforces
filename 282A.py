import sys
input = sys.stdin.readline

ans = 0
t = int(input())
for _ in range(t):
    s = str(input()).strip()
    if s == "++X" or s == "X++":
        ans += 1
    else:
        ans -= 1
print(ans) 