import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = str(input()).strip()
    ans, d1, d2, d3 = 0, 0, 0, 0
    for x in s:
        if x == '1':
            d1 += 1
        elif x == '3':
            d3 += 1
    ans = d1 + d3
    for x in s:
        if x == '2':
            d2 += 1
        elif x == '1':
            d1 -= 1
        elif x == '3':
            d3 -= 1
        ans = max(ans, d1 + d2 + d3)
    print(len(s) - ans)
    