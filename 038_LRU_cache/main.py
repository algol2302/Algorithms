import time
from collections import OrderedDict
from functools import lru_cache, wraps


class LRUCache0:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def __setitem__(self, key, value):
        # uncomment it if you need check setting a key-value pair:
        # print(f'Setting a new cached pair: ({key}, {value})')
        self.cache[key] = value
        self.cache.move_to_end(key=key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def __getitem__(self, key):
        return self.cache[key]

    def __repr__(self):
        return f"<LRU({self.capacity}): {self.cache!s}>"

    def __call__(self, func):
        decorator_self = self
        @wraps(func)
        def wrapper(key):
            # we suppose that a function will have just one argument
            try:
                value = decorator_self[key]
            except KeyError:
                value = func(key)
                decorator_self[key] = value
            return value

        return wrapper


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    # Delete node from double linked-list
    def _delete(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # Over here the result task is being done
    def _llist(self, key):
        current = self.head

        while True:
            if current.key == key:
                node = current
                self._delete(node)
                self._insert(node)
                break
            else:
                current = current.next

    def __call__(self, func):
        decorator_self = self
        # The cache presents with the help
        # of Linked List
        @wraps(func)
        def wrapper(key):
            if key in decorator_self.cache:
                decorator_self._llist(key)
                return decorator_self.cache[key]

            if len(decorator_self.cache) > decorator_self.capacity:
                n = decorator_self.head.next
                decorator_self._delete(n)
                del decorator_self.cache[n.key]

            # Compute and cache and node to see whether
            # the following element is present or not
            # based on the given input.
            result = func(key)
            decorator_self.cache[key] = result
            node = Node(key, result)
            decorator_self._insert(node)

            return result
        return wrapper

    def __repr__(self):
        return f"<LRU({self.capacity}): {self.cache!s}>"

def fib_slow(n):
    if n < 2:
        # print(n)
        return n
    res = fib_slow(n-1) + fib_slow(n-2)
    # print(res)
    return res

@LRUCache0(capacity=38)
def fib_0(n):
    if n < 2:
        # print(n)
        return n
    res = fib_0(n-1) + fib_0(n-2)
    # print(res)
    return res

@LRUCache1(capacity=38)
def fib_1(n):
    if n < 2:
        # print(n)
        return n
    res = fib_1(n-1) + fib_1(n-2)
    # print(res)
    return res

@lru_cache
def fib(n):
    if n < 2:
        # print(n)
        return n
    res = fib(n-1) + fib(n-2)
    # print(res)
    return res


def main():
    # tests LRUCache0:
    print('tests LRUCache0:')
    cache = LRUCache0(capacity=2)
    cache['a'] = 'a'
    cache['b'] = 'b'
    print(cache, cache['a'])
    cache['c'] = 'c'
    try:
        print(cache, cache['a'])
    except KeyError as exc:
        print(cache, 'there is not a')

    print('-------------------')
    print('test lru_cache_0 decorator:')
    # test lru_cache_0:
    t0 = time.time()
    fib_slow(38)
    t1 = time.time()
    print(f"Slow fib: {t1 - t0} sec")

    t0 = time.time()
    fib_0(38)
    t1 = time.time()
    print(f"Version #0 LRU cached fib: {t1 - t0} sec")

    t0 = time.time()
    fib_1(38)
    t1 = time.time()
    print(f"Version #1 LRU cached fib: {t1 - t0} sec")

    t0 = time.time()
    fib(38)
    t1 = time.time()
    print(f"Built-in LRU cached fib: {t1 - t0} sec")

if __name__ == '__main__':
    main()
