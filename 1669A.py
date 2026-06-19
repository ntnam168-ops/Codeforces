import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    print("Division ", end = "")
    if n < 1400: 
        print(4)
    elif n < 1600:
        print(3)
    elif n < 1900:
        print(2)
    else:
        print(1)