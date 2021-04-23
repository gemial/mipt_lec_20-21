import visualisation.vis

def z(s: str):
    str_in = list(s)
    result = list([0] * len(str_in))
    r = l = 0
    for i in range(1, len(str_in)):
        if i < r:
            result[i] = min(r - i, result[i - l])
            if i + result[i] < r:
                continue
        while i + result[i] < len(str_in) and str_in[result[i]] == str_in[i + result[i]]:
            len(str_in)
            result[i] += 1

        if i + result[i] > r:
            l, r = i, i + result[i]

    return result


if __name__ == "__main__":
    s = 'ababcababcffffababcabababcababc'
    print(' ', '  '.join(s))
    print(''.join(map(lambda x: f'{x:3}', z(s))))