import sys
input = sys.stdin.readline

def check(n):
    s = str(n)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

n = int(input())
n += 1
while not check(n):
    n += 1
print(n)