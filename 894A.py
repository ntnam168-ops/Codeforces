import sys
input = sys.stdin.readline

s = str(input())
q, qa, qaq = 0, 0, 0
for k in s:
    if k == 'Q':
        q += 1
        qaq += qa
    elif k == 'A':
        qa += q
print(qaq)