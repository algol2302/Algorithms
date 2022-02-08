from typing import Any


class Stack:
    """LIFO - last in first out"""

    def __init__(self, *args: Any) -> None:
        self.values = [*args]

    def __repr__(self):
        return f"{self.values!r}"

    def append(self, item) -> None:
        self.values.append(item)

    def extend(self, *args: Any) -> None:
        self.values.extend(*args)

    def pop(self) -> Any:
        return self.values.pop(-1)


class Queue(Stack):
    """FIFO - first in first out"""

    def pop(self) -> Any:
        return self.values.pop(0)


def check_stack():
    stack = Stack(3, "a", 42, "fiz", "baz", 99)
    print(f"Initial stack: {stack}")

    print(f"Extract first element: {stack.pop()}, rest elements: {stack}")

    new_item = "c"
    stack.append(new_item)
    print(f"Add element {new_item}, result: {stack}")

    new_items = (22, 34.4, "d")
    stack.extend(new_items)
    print(f"Add elements {new_items}, result: {stack}")


def check_queue():
    queue = Queue(3, "a", 42, "fiz", "baz", 99)
    print(f"Initial queue: {queue}")

    print(f"Extract first element: {queue.pop()}, rest elements: {queue}")

    new_item = "c"
    queue.append(new_item)
    print(f"Add element {new_item}, result: {queue}")

    new_items = (22, 34.4, "d")
    queue.extend(new_items)
    print(f"Add elements {new_items}, result: {queue}")


if __name__ == "__main__":
    check_stack()
    print("--------")
    check_queue()
