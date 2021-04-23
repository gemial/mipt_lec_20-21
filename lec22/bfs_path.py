from queue import Queue

def read_graph(filename):
    N = M = None
    G = {}
    for line in open(filename, 'r'):
        if N is None:
            N, M = map(int, line.split())
            continue
        v1, v2 = line.split()
        print(v1, v2)
        for v in v1, v2:
            if v + '0' not in G:
                G[v + '0'] = set()
                G[v + '1'] = set()

        G[v1 + '0'].add(v2 + '1')
        G[v2 + '0'].add(v1 + '1')
        G[v1 + '1'].add(v2 + '0')
        G[v2 + '1'].add(v1 + '0')
    return G

def read_graph(f):
    G = {}
    for i in 'absdefgh':
        for j in '12345678':
            G[i+j+'0'] = set()
            G[i+j+'1'] = set()

    for x in G:
        for y in G:
            if abs((ord(x[0]) - ord(y[0])) * (ord(x[1]) - ord(y[1])) * (ord(x[2]) - ord(y[2]))) == 2:
                G[x].add(y)
                G[y].add(x)
    return G


def bfs(G, start):
    start = start + '0'
    path = {v: None for v in G}
 
    q = Queue()
    q.put(start)
    path[start] = [start]

    while not q.empty():
        v = q.get()
        for neighbor in G[v]:
            if path[neighbor] is None:
                q.put(neighbor)
                path[neighbor] = path[v] + [neighbor]

    return path


G = read_graph('graph.txt')
dist = bfs(G, 'a1')
for v in G:
    if v[-1] == '0':
       print(v, dist[v]) 

