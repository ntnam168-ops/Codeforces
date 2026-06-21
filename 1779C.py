import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    val, ans, pq = 0, 0, []
    for i in range(m - 1, 0, -1):
        val += a[i]
        heapq.heappush(pq, -a[i])
        if val > 0:
            x = -heapq.heappop(pq)
            val -= x * 2
            ans += 1
    val, pq = 0, []
    for i in range(m, n):
        val += a[i]
        heapq.heappush(pq, a[i])
        if val < 0:
            x = heapq.heappop(pq)
            val -= x * 2
            ans += 1
    print(ans)