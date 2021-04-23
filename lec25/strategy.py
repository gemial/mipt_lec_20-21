def read_graph():
    N, M = map(int, input().split())
    G = [[] for i in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
    return G


def dfs(G, x, res):
    for v in G[x]:
        if res[v] == '':
            dfs(G, v, res)
        if res[v] == 'L':
            res[x] = 'W'
            break
    else:
        res[x] = 'L'


G = read_graph()
print(G)
res = ['' for i in range(len(G))]
res[-1] = 'L'
dfs(G, 0, res)   
print(res)

