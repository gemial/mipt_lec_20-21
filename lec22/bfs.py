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
    distances = {v: None for v in G}
 
    q = Queue()
    q.put(start)
    distances[start] = 0

    while not q.empty():
        v = q.get()
        for neighbor in G[v]:
            if distances[neighbor] is None:
                q.put(neighbor)
                distances[neighbor] = distances[v] + 1
    return distances


G = read_graph('graph.txt')
dist = bfs(G, 'A')
print(path(G, 'A', 'J')) 

