from queue import Queue
from random import randint
import heapq
from time import time

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
                G[v] = {}
        G[v1][v2] = G[v2][v1] = randint(10, 99)
    return G


def deikstra_1(G, start):
    distances = {v: float('+inf') for v in G}
 
    q = Queue()
    q.put(start)
    distances[start] = 0

    while not q.empty():
        v = q.get()
        for neighbor in G[v]:
            tmp = distances[v] + G[v][neighbor]
            if distances[neighbor] > tmp:
                q.put(neighbor)
                distances[neighbor] = tmp
    return distances


def deikstra_2(G, start):
    heap = []
    distances = {v: float('+inf') for v in G}
 
    distances[start] = 0
    heapq.heappush(heap, (0, start) )    

    while len(heap) > 0:
        v = heapq.heappop(heap)[1]
        for neighbor in G[v]:
            tmp = distances[v] + G[v][neighbor]
            if distances[neighbor] > tmp:
                heapq.heappush(heap, (tmp, neighbor)) 
                distances[neighbor] = tmp
    return distances


G = read_graph('graph.txt')
print(G)
t = time()
dist1 = deikstra_1(G, 'A')
print(f'{time() - t:.7f}')
t = time()
dist2 = deikstra_2(G, 'A')
print(f'{time() - t:.7f}')
for i in G:
    print(dist1[i], dist2[i], dist1[i] - dist2[i], sep='\t')

