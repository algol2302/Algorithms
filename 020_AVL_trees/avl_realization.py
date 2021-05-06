from numbers import Number
from typing import Any


class Node:

    def __init__(self, data: Number, parent: Any):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.height = 0

    def __repr__(self):
        return f"Node with data: {self.data!r}"


class AVLTree:

    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def insert(self, data: Number) -> None:
        if not self.root:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data: Number, node: Node):
        # we insert into left subtree
        if data < node.data:
            # check if there is a left child
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
                node.height = max(
                    self.calculate_height(node.left_child),
                    self.calculate_height(node.right_child)
                ) + 1
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)
                node.height = max(
                    self.calculate_height(node.left_child),
                    self.calculate_height(node.right_child)
                ) + 1

        # after every insertion we have to check tree balance
        self.handle_violation(node)

    def calculate_height(self, node: Node):
        pass

    def handle_violation(self, node: Node):
        pass


def main():
    bst = AVLTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(-5)
    bst.insert(1)
    bst.insert(99)
    bst.insert(34)
    bst.insert(1000)

    bst.remove(99)

    print(f"Max value: {bst.get_max_value()}")
    print(f"Min value: {bst.get_min_value()}")
    bst.traverse()


if __name__ == '__main__':
    main()
