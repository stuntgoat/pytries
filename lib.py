"""
Some helper functions
"""
from string import lowercase

def name_factory(count):
    length = 1
    while True:
        for i in lowercase:
            if not count:
                return
            yield i * length
            count -= 1
        length += 1
