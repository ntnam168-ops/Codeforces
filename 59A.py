s = str(input())
low, up = 0, 0
for k in s:
    if k >= "a" and k <= "z":
        low += 1
    else:
        up += 1
t = ""
if low >= up:
    for k in s:
        if k >= "A" and k <= "Z":
            t += k.lower()
        else:
            t += k
else:
    for k in s:
        if k >= "a" and k <= "z":
            t += k.upper()
        else:
            t += k
print(t)