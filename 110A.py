import sys
input = sys.stdin.readline

ans = 0
s = str(input()).strip()
for x in s:
    if x == '4' or x == '7':
        ans += 1
if ans == 4 or ans == 7:
    print("YES")
else:
    print("NO")