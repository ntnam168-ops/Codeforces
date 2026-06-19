n, k = map(int, input().split())
l, c = n - int(n / 2), int(n / 2)
if k <= l:
    print(k * 2 - 1)
else:
    k -= l
    print(k * 2)