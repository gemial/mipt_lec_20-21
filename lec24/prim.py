heap = []


def shift_up(id):
    if id == 0:
        return
    p = (id - 1) // 2
    if heap[id][0] < heap[p][0]:
        heap[id], heap[p] = heap[p], heap[id]
        heap[id][1], heap[p][1] = heap[p][1], heap[id][1]
        shift_up(p)


def shift_down(id):
    next = heap[id][0]
    if len(heap) > 2 * id + 1 and heap[2 * id + 1][0] < next:
        next = heap[2 * id + 1][0]
    if len(heap) > 2 * id + 2 and heap[2 * id + 2][0] < next:
        next = heap[2 * id + 2][0]
    if heap[id][0] == next:
        return
    if heap[2 * id + 1][0] == next:
        p = 2 * id + 1
        heap[id], heap[p] = heap[p], heap[id]
        heap[id][1], heap[p][1] = heap[p][1], heap[id][1]
        shift_down(p)
        return
    p = 2 * id + 2
    heap[id], heap[p] = heap[p], heap[id]
    heap[id][1], heap[p][1] = heap[p][1], heap[id][1]
    shift_down(p)


def push(el):
    heap.append(el)
    shift_up(len(heap) - 1)


def pop():
    a = heap[0]
    heap[0] = heap[-1]
    heap[0][1] = 0
    heap.pop()
    if not empty():
        shift_down(0)
    return a


def empty():
    return len(heap) == 0


def prim(G):
    start = next(iter(G.keys()))

    min_tree = []
    min_value = 0
    n = 0
    min_distances = {}
    for x in G:
        if x != start:
            min_distances[x] = [float('+inf'), n, None, x]
            n += 1

    used = {start}
    for v in G[start]:
        min_distances[v][0] = G[start][v]
        min_distances[v][2] = start
    for k, v in min_distances.items():
        push(v)
    while not empty():
        print(heap)
        nxt = pop()
        used.add(nxt[3])
        min_value += nxt[0]
        min_tree.append((nxt[2], nxt[3]))
        for v in G[nxt[3]]:
            if v not in used:
                if G[nxt[3]][v] < min_distances[v][0]:
                    min_distances[v][0] = G[nxt[3]][v]
                    min_distances[v][2] = nxt[3]
                    shift_up(min_distances[v][1])

    return min_tree, min_value


G = {}
N, M = map(int, input().split())
for _ in range(M):
    v1, v2, w = input().split()
    if v1 not in G:
        G[v1] = {}
    if v2 not in G:
        G[v2] = {}
    G[v1][v2] = float(w)
    G[v2][v1] = float(w)

print(prim(G))
