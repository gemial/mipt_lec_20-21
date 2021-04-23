from queue import Queue

def read_graph(filename):
    N = M = None
    G = {}
    for line in open(filename, 'r'):
        if N is None:
            N, M = map(int, line.split())
            continue
        v1, v2 = line.split()
        for v in v1, v2:
            if v not in G:
                G[v] = set()
        G[v1].add(v2)
        G[v2].add(v1)
    return G



def bfs(G, start):
    path = {v: None for v in G}
 
    q = Queue()
    q.put(start)
    path[start] = ['A']

    while not q.empty():
        v = q.get()
        for neighbor in G[v]:
            if path[neighbor] is None:
                q.put(neighbor)
                path[neighbor] = path[v] + [neighbor]
    return path


def bfs(G, start):
    parent = {v: None for v in G}
 
    q = Queue()
    q.put(start)
    parent[start] = None

    while not q.empty():
        v = q.get()
        for neighbor in G[v]:
            if parent[neighbor] is None:
                q.put(neighbor)
                parent[neighbor] = v
            elif parent[v] != neighbor:
                # мы нашли цыкл
                pass
            
    return parent


G = read_graph('graph.txt')
dist = bfs(G, 'A')
print(dist)

