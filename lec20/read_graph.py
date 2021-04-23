N, M = map(int, input().split())

G = [[0] * N for _ in range(N)]
V_names = []

for _ in range(M):
    v1, v2 = input().split()
    for v in (v1, v2):
        if v not in V_names:
            V_names.append(v)
    i1 = V_names.index(v1)
    i2 = V_names.index(v2)
    G[i1][i2] = 1
    G[i2][i1] = 1

print(' '.join(V_names))
for line in G:
    print(' '.join(map(str, line)))

for V_ind, V_name in enumerate(V_names):
    print(V_name, 
          G[V_ind].count(1), 
          *[V_names[i] for i in range(N) if G[V_ind][i] == 1])


