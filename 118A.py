import sys
input = sys.stdin.readline

s = str(input())
s = s.lower().strip()
for k in s:
    if k != 'a' and k != 'e' and k != 'u' and k !='i' and k != 'o' and k != 'y':
        print('.', end = "")
        print(k, end = "")