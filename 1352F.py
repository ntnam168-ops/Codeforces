import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    if y % 2 == 1:
        s = "" 
        for i in range(x):
            s += '0'
        for i in range(y + 1):
            if i % 2 == 0:
                s += '0'
            else:
                s += '1'
        for i in range(z):
            s += '1'
        print(s)
    else:
        s = "" 
        if x > z:
            for i in range(x):
                s += '0'
            for i in range(y + 1):
                if i % 2 == 0:
                    s += '0'
                else:
                    s += '1'
            s = s[:len(s) - 1]
            for i in range(z):
                s += '1'
            s += '0'
        else:
            
            for i in range(z):
                s += '1'
            for i in range(y + 1):
                if i % 2 == 0:
                    s += '1'
                else:
                    s += '0'
            s = s[:len(s) - 1]
            for i in range(x):
                s += '0'
            s += '1'
        print(s)
