import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = str(input()).strip()
    ans = 0
    while True:
        sum = 0
        for x in s:
            sum += ord(x) - ord('0')
        if sum < 10:
            break
        d = 0
        for i in range(len(s)):
            if ord(s[i]) - ord('0') - (i == 0) > ord(s[d]) - ord('0') - (d == 0):
                d = i
        ans += 1
        if d == 0:
            s = "1" + s[1 :]
        else:
            s = s[: d] + "0" + s[d + 1 :]
    print(ans)
    