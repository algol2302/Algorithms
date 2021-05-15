from numbers import Number
from typing import Any
from collections import namedtuple

Color = namedtuple("Color", ["RED", "BLACK"])(1, 2)


class Node:

    def __init__(self, data: Number, parent: Any = None, color=Color.RED):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        return f"node with data: {self.data!r} and color: {self.color!r}"


class RedBlackTree:

    def __init__(self):
        self.root = None

    def insert(self, data: Number):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data: Number, node: Node):

        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                self.settle_violation(node.left_node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                self.settle_violation(node.right_node)

    def settle_violation(self, node: Node):
        # TODO
        pass

    def traverse(self):
        if self.root:
            self.in_order_traversal(self.root)

    def in_order_traversal(self, node: Node):

        if node.left_node:
            self.in_order_traversal(node.left_node)

        print(node)

        if node.right_node:
            self.in_order_traversal(node.right_node)


def main():
    a = Node(1)
    print(a)


if __name__ == '__main__':
    main()
