# LIFO

class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return f"Stack: {self.stack!r}, size :{self.stack_size()}"

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack_size() < 1:
            return
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
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
