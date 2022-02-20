# coding=utf-8

# 图算法 广度优先算法
from collections import deque


def find_ending(letter):
    while len(queue) > 0:
        name = queue.pop()
        if name not in checked:
            checked.append(name)
            if is_end_letter(name, letter):
                return name
            else:
                if name in address_book:
                    queue.extend(address_book[name])
    return None


def is_end_letter(word, letter):
    return word[-1] == letter


address_book = {
    'you': ['lxz', 'jc', 'fqy'],
    'lxz': ['cxz', 'xxx', 'lzj', 'hzs'],
    'jc': ['yzy', 'lzm'],
    'lzj': ['xy', 'lx']
}

checked = []
queue = deque()
queue.extend(address_book['you'])

print find_ending('x')
