import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x, y, z, t = 0, 0, 0, 0
for i in a:
    if i == 1:
        x += 1
    elif i == 2:
        y += 1
    elif i == 3:
        z += 1
    else:
        t += 1
ans = t + min(x, z) + y // 2
y %= 2
d = min(x, z)
x -= d
z -= d
if z > 0:
    ans += z + y
elif x > 0:
    if y:
        ans += 1
        x -= min(x, 2)
    ans += x // 4
    if x % 4:
        ans += 1
else:
    ans += y
print(ans)