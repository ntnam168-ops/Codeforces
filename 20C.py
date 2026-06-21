import sys, heapq
input = sys.stdin.readline

pq = []
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
d = [int(1e18)] * (n + 1)
pr = [0] * (n + 1)
for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))
d[1] = 0
heapq.heappush(pq, (0, 1))
while pq:
    val, u = heapq.heappop(pq)
    if val != d[u]:
        continue
    for (v, w) in g[u]:
        if d[v] > d[u] + w:
            pr[v] = u
            d[v] = d[u] + w
            heapq.heappush(pq, (d[v], v))
if d[n] == int(1e18):
    print(-1)
    exit(0)
ar = []
while n != 1:
    ar.append(n)
    n = pr[n]
ar.append(1)
ar = list(reversed(ar))
for x in ar:
    print(x, end = " ")
