from queue import Queue
from time import sleep
G = {}

letters = 'abcdefgh'
numbers = '12345678'


for w in letters:
    for h in numbers:
        G[''.join((w, h))] = set()

for x in G:
    for y in G:
        if abs((ord(x[0]) - ord(y[0])) * (ord(x[1]) - ord(y[1]))) == 2:
            G[x].add(y)
            G[y].add(x)



def calc_pathes(G, start, end):
    pathes = {v:None for v in G}
    parent = {x:None for x in G}
    used = set()
    q = Queue()
    q.put(start)
    pathes[start] = [start]
    while not q.empty():
        vertex = q.get()
        used.add(vertex)
        for neighbor in G[vertex]:
            if neighbor not in used:
                q.put(neighbor)
                parent[neighbor] = vertex
                pathes[neighbor] = pathes[vertex].copy()
                pathes[neighbor].append(neighbor)
                if neighbor == end:
                    break

    return pathes

def table_print(data):
    print('\033[0;0H\033[48:2:127:127:255m\033[0J', sep='')

    for i in range(8):
        print('\033[48:2:127:127:255m ', chr(ord('8') - i), end=' ', sep='')
        for j in range(8):
            if (i + j) % 2:
                print('\033[48:2:255:255:255m\033[30m', end='   ')
            else:
                print('\033[48:2:0:0:0m\033[38m', end='   ')
        print('\033[0m')

    print('\033[48:2:127:127:255m   ', '  '.join(map(chr, range(97, 105))), end='', sep='')

    for n, e in enumerate(data):
        i, j = ord(e[0]) - ord('a'), ord(e[1]) - ord('1')
        print('\033[{};{}H'.format(9 - j, 5 + 3 * i), end='')
        if (i + j) % 2:
            print('\033[1;48:2:0:0:0;38:2:255:255:255m', n, sep='')
        else:
            print('\033[1;48:2:255:255:255;38:2:0:0:0m', n, sep='')


    print('\033[11;0H\033[0m\033[0J', data)

start, end = input().split()
pathes = calc_pathes(G, start, end)
table_print(pathes[end])
