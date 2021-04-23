N, M = map(int, input().split())

G = [[] for _ in range(N)] 
for _ in range(M):
    v1, v2 = map(ord, input().split())
    v1 -= 65
    v2 -= 65
    G[v1].append(v2)
    G[v2].append(v1)

#for i, j in enumerate(G):
#    print(i, len(j), j)

edges = []
offset = [0]
for i in G:
    for e in i:
        edges.append(e)
    offset.append(len(edges))

# print(offset)
# print(edges)

for v_i in range(len(offset) - 1):
    print(
          v_i,
          offset[v_i + 1] - offset[v_i],
          *edges[offset[v_i]:offset[v_i + 1]]
         ) 
    


