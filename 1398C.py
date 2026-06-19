import sys
input = sys.stdin.readline

t = int(input())
mp = [0] * (int(9e5) + 1)
for _ in range(t):
    n = int(input())
    s = str(input()).strip()
    a = []
    for k in s:
        a.append(ord(k) - ord('0'))
    s, ans = 0, 0
    mp[0] = 1
    for i in range(n):
        s += a[i]
        ans += mp[s - (i + 1)]
        mp[s - (i + 1)] += 1
    s = 0
    for i in range(n):
        s += a[i]
        mp[s - (i + 1)] = 0
    print(ans)