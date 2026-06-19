import sys
input = sys.stdin.readline

tt = int(input())
for _ in range(tt):
    s = str(input()).strip()
    t = sorted(s)
    t = str().join(t)
    if t[0] == t[-1]:
        print("NO")
    else:
        print("YES")
        if t != s:
            for i in range(len(t)):
                print(t[i], end="")
            print()
        else:
            for i in range(len(t) - 1, -1, -1):
                print(t[i], end="")
            print()