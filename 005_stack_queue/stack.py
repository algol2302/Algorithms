# LIFO

class Stack:
    def __init__(self):
        self.stack = []
        # for max_value in stack
        self.max_stack = []

    def __repr__(self):
        return (
            f"Stack: {self.stack!r}, size :{self.stack_size()}, "
            f"max_value: {self.get_max_item()}, max_stack: {self.max_stack!r}"
        )

    def push(self, data):
        self.stack.append(data)

        if not self.max_stack:
            self.max_stack.append(data)
            return

        self.max_stack.append(max(data, self.max_stack[-1]))

    def pop(self):
        if self.stack_size() < 1:
            return
        self.max_stack.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

    def get_max_item(self):
        if self.max_stack:
            return self.max_stack[-1]


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    print(stack)
    print(f"Popped item: {stack.pop()}")
    print(stack)
    print(f"Peek item: {stack.peek()}")
    print(stack)
    print(f"Popped item: {stack.pop()}")
    print(stack)
    print(f"Popped item: {stack.pop()}")
    print(stack)
    print(f"Popped item: {stack.pop()}")
    print(stack)


if __name__ == '__main__':
    main()
