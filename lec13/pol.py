
__STACK = []

def push(data):
    ''' push data to stack'''
    __STACK.append(data)

def pop():
    ''' take last pushed data from stack'''
    return __STACK.pop()

def top():
    ''' get last pushed data '''
    return __STACK[-1]

def is_empty():
    ''' return True is stack is empty '''
    return len(__STACK) == 0

if __name__ == "__main__":
    expression = '2 * ( 3 + 5 ) * 8 - 1'.split()

    for element in 

    for element in expression:
        if element == '+':
            push(pop() + pop())
        elif element == '*':
            push(pop() * pop())
        elif element == '-':
            push(-pop() + pop())
        elif element == '/':
            push(1 / pop() * pop())
        else:
            push(float(element))

    result = pop()
    if is_empty():
        print(result)
    else:
        print('Error wrong expression')
        print(result)
        while not is_empty():
            print(pop())
