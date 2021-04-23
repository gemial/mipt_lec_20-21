N, M = map(int, input().split())

G = [[] for _ in range(N)] 
for _ in range(M):
    v1, v2 = map(ord, input().split())
    v1 -= 65
    v2 -= 65
    G[v1].append(v2)
    G[v2].append(v1)

for i, j in enumerate(G):
    print(i, len(j), *j)

