import sys, math
input = sys.stdin.readline

n = int(input())
ans = 0
for i in range(max(1, n - 10), n + 1):
    for j in range(i, n + 1):
        for k in range(j, n + 1):
            ans = max(ans, math.lcm(i, math.lcm(j, k)))
print(ans)