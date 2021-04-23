from random import randint


def BinTree():
    return {'root': None, 'height'['root':0]}


def Node(value):
    return {
        'left': None,
        'right': None,
        'value': value,
        'height': {'left':0, 'right':0}
    }


def add_to_tree(tree, value):
    if tree['root'] is None:
        tree['root'] = Node(value)
    else:
        tree['height']['root'] = add_to_node(tree['root'], value)
        check_node(tree, tree['root'], 'root')


def add_to_node(node, value):
    if value > node['value']:
        if node['right'] is None:
            node['right'] = Node(value)
            node['height']['right'] = 1
        else:
            node['height']['right'] = add_to_node(node['right'], value)
        check_node(node, node['right'], 'right')
    else:
        if node['left'] is None:
            node['left'] = Node(value)
            node['height']['left'] = 1
        else:
            node['height']['left'] = add_to_node(node['left'], value)
        check_node(node, node['left'], 'left')
    return max(node['height']) + 1


def print_tree(tree):
    print_node(tree['root'])
    print()


def print_node(node, x=1):
    if node is None:
        return
    print_node(node['left'], x + 1)
    print(f'\033[1;3{x}m\033[{x}B',
          node['value'],
          f'\033[{x}A\033[0m',
          sep='',
          end='')
    print_node(node['right'], x + 1)


def check_node(parent, node, side):
    if node is None:
        return 0
    h = node['height']['left'] - node['height']['right']
    if h == 2:
        if node['left']['height']['left'] - node['left']['height']['right'] == 1:
            node['height']['left'] = node['left']['height']['right']
            node['left']['height']['right'] = max(node['height']) + 1
            parent[side] = node['left']
            node['left'] = node['left']['right']
            parent[side]['right'] = node
        else:
            node['height']['left'] = node['left']['right']['height']['right']
            node['left']['height']['right'] = node['left']['right']['height']['left']
            node['left']['right']['height']['left'] = max(
                node['left']['height']) + 1
            node['left']['right']['height']['right'] = max(node['height']) + 1
            parent[side] = node['left']['right']
            node['left']['right'] = parent[side]['left']
            parent[side]['left'] = node['left']
            node['left'] = parent[side]['right']
            parent[side]['right'] = node
    if h == -2:
        if node['right']['height']['left'] - node['right']['height']['right'] == -1:
            node['height']['right'] = node['right']['height']['left']
            node['right']['height']['left'] = max(node['height']) + 1
            parent[side] = node['right']
            node['right'] = node['right']['left']
            parent[side]['left'] = node
        else:
            node['height']['right'] = node['right']['left']['height']['left']
            node['right']['height']['left'] = node['right']['left']['height']['right']
            node['right']['left']['height']['right'] = max(
                node['right']['height']) + 1
            node['right']['left']['height']['left'] = max(node['height']) + 1
            parent[side] = node['right']['left']
            node['right']['left'] = parent[side]['right']
            parent[side]['right'] = node['right']
            node['right'] = parent[side]['left']
            parent[side]['left'] = node
    parent[side]['height'][side] -= 1
    # return max() + 1


tree = BinTree()
for _ in range(15):
    r = randint(100, 999)
    print('\033[0;0H\033[0J', r)
    add_to_tree(tree, r)
    print_tree(tree)
    input()

print_tree(tree)
