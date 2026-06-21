import sys
input = sys.stdin.readline

n, k = map(int, input().split())
g = [[] for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n)]
pa = [-1] * n
q, qu = [], []

def dfs():
    global q, qu
    qu = [0]
    while(len(qu) > 0):
        u = qu[len(qu) - 1] 
        q.append(u)
        qu.pop()
        for v in g[u]:
            if v != pa[u]:
                pa[v] = u
                qu.append(v)          
        dp[u][0] = 1
    q = list(reversed(q))
    for u in q:
        dp[u][0] = 1
        for v in g[u]:
            if v != pa[u]:
                for i in range(1, k + 1):
                    dp[u][i] += dp[v][i - 1]

ans, ans1 = 0, 0

def cal(u, p):
    global ans, ans1
    for u in q:
        ans += dp[u][k]
        for v in g[u]:
            if v != pa[u]:
                for i in range(1, k):
                    ans1 += dp[v][i - 1] * (dp[u][k - i] - dp[v][k - i - 1])

for i in range(n - 1):
    u, v = map(int, input(). split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)
dfs()
cal(0, -1)
print(ans + ans1 // 2)
