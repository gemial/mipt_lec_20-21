
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
    s = '(x+(x*[a+b]])[25]))'
    
    for ch in s:
        if ch in '[(':
            push(ch)
        elif ch == ']':
            if is_empty() or pop() != '[':
                print('ERROR')
                break
        elif ch == ')':
            if is_empty() or pop() != '(':
                print('ERROR')
                break
        else:
            pass
while not is_empty():
    print(pop())

print("END")


