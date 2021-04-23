def read_graph(filename):
    N = M = None
    G = {}
    for line in open(filename, 'r'):
        if N is None:
            N, M = map(int, line.split())
        v1, v2 = line.split()
        for v in v1, v2:
            if v not in G:
                G[v] = []
        G[v1].append(v2)
        G[v2].append(v1)
    return G

def dfs(G, vertex, used=None):
    if used is None:
        used = set()
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used)


G = read_graph('graph.txt')
used = set()
for vertex in G.keys():
    if vertex not in used:
        dfs(G, vertex, used)
        N += 1

