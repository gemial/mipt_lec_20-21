from random import randint

def LinkedList():
    return {'first': None, 'last':None}


def Node(value):
    return {'value':value, 'next':None, 'pervious':None}


def add_to_list(value, l_list):
    new_node = Node(value)
    new_node['next'] = l_list['first']
    l_list['first'] = new_node


def pop_from_list(l_list):
    res = l_list['first']['value']
    l_list['first'] = l_list['first']['next']
    return res

def printlist(l_list):
    current_node = l_list['first']
    while current_node is not None:
        print(current_node['value'], end=' ')
        current_node = current_node['next']
        if current_node == l_list['first']:
            break
    print()
    

def insert_value(node, value):
    new_node = Node(value)
    new_node['next'] = node['next']
    node['next'] = new_node


l = LinkedList()
for _ in range(10):
    add_to_list(randint(100, 999), l)

printlist(l)

current_node = l['first']
while current_node is not None:
    if current_node['value'] % 2:
        insert_value(current_node, 0)
    last = current_node
    current_node = current_node['next']

last['next'] = l['first']

printlist(l)

