import time
import traceback as tb
import gc
import sys
from random import shuffle


class VisualListElement:

    def __init__(self, value, color=0, format='', **kwargs):
        self.value = value
        self.color = color
        self.__colors = [0, 2, 4]
        self.__format_repr = '\033[4{1}m{0:' + format + '}\033[0m'
        self.__format_str = '{0:' + format + '}'

    def __repr__(self):
        return self.__format_repr.format(self.value, self.__colors[self.color])

    def __str__(self):
        return self.__format_str.format(self.value, self.__colors[self.color])


class VisualList:
    numbers = 0
    delay = 0.05

    def __init__(self, data=None, **kwargs):
        if data is None:
            data = []
        self._st_data = kwargs
        self._data = [VisualListElement(el, **kwargs) for el in data]
        self._cur_line = 0
        self.__string = VisualList.numbers
        if 'name' in kwargs:
            self.__name = kwargs['name']
        else:
            self.__name = tb.extract_stack()[-2].line.split('=')[0].strip()
        VisualList.numbers += 1
        self.__out()

    @staticmethod
    def __check__():
        pass

    def set_name(self, name):
        self.__name = name

    def __recolor(self, dop=0):
        tmp = tb.extract_stack()[-3 - dop].lineno
        time.sleep(self.delay)
        if tmp != self._cur_line:
            # time.sleep(delay)
            self._cur_line = tmp
            for el in self._data:
                el.color = 0

    def __out(self):
        self.__check__()
        print(f'\033[s\033[H', end='', sep='', file=sys.stderr)
        if self.__string:
            print(f'\033[{self.__string}B', end='', sep='', file=sys.stderr)
        print(self.__name,
              ', '.join(map(repr, self._data)),
              end='', sep=': ', file=sys.stderr)
        print('\033[0K\033[u', end='', sep='', file=sys.stderr, flush=True)
        self.__recolor(1)

    def append(self, value):
        self._data.append(VisualListElement(value, **self._st_data))
        self.__out()

    def __getitem__(self, i):
        self.__recolor()
        self._data[i].color = 1
        self.__out()
        return self._data[i].value

    def get(self, i):
        self.__recolor()
        self._data[i].color = 1
        self.__out()
        return self._data[i].value

    def __setitem__(self, i, value):
        self.__recolor()
        self._data[i].color = 2
        self._data[i].value = value
        self.__out()
        return self._data[i].value

    def __str__(self):
        self.__out()
        return ', '.join(map(str, self._data))

    def __len__(self):
        self.__out()
        return len(self._data)

    def extend(self, other):
        for el in other:
            self._data.append(VisualListElement(el))
            self._data[-1].color = 1
            self.__out()
            time.sleep(self.delay)

    def clear(self):
        self._data.clear()
        self.__out()

    def __iter__(self):
        self._curitem = -1
        return self

    def __next__(self):
        self._curitem += 1
        if self._curitem >= len(self._data):
            raise StopIteration()
        self._data[self._curitem].color = 1
        self.__out()
        return self._data[self._curitem].value

    def shuffle(self):
        __builtins__['list'] = _base_list
        shuffle(self._data)
        self.__out()
        __builtins__['list'] = VisualList


_base_list = __builtins__['list']
__builtins__['list'] = VisualList

# print('\033[s\033[H\033[0J\033u')
