import visualisation.vis

def pref(s:str):
    str_in = list(s)
    result = list([0 for _ in s])
    for i in range(1, len(s)):
        p = result[i - 1]
        while p != 0 and str_in[p] != str_in[i]:
            p = result[p - 1]
        if str_in[i] == str_in[p]:
            result[i] = p + 1
        else:
            result[i] = 0
    return result


if __name__ == "__main__":
    s = 'ababcababcffffababcabababcababc'
    print(' ', '  '.join(s))
    print(''.join(map(lambda x: f'{x:3}', pref(s))))