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

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data: Number, node: Node):

        if not node:
            return

        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:
            # we have found the node we want to remove
            # case 1) the node is leaf node
            if not node.left_child and not node.right_child:
                print(f"Removing a leaf node...{node}")
                parent = node.parent

                if parent and parent.left_child == node:
                    parent.left_child = None

                if parent and parent.right_child == node:
                    parent.right_child = None

                if not parent:
                    self.root = None

                del node
                # after every deletion we have to check tree balance
                self.handle_violation(parent)

            elif not node.left_child and node.right_child:
                print(f"Removing a node with single right child")

                parent = node.parent

                if parent and parent.left_child == node:
                    parent.left_child = node.right_child
                elif parent and parent.right_child == node:
                    parent.right_child = node.right_child
                else:
                    self.root = node.right_child

                node.right_child.parent = parent
                del node
                # after every deletion we have to check tree balance
                self.handle_violation(parent)

            elif node.left_child and not node.right_child:
                print(f"Removing a node with single left child")

                parent = node.parent

                if parent and parent.left_child == node:
                    parent.left_child = node.left_child
                elif parent and parent.right_child == node:
                    parent.right_child = node.left_child
                else:
                    self.root = node.left_child

                node.left_child.parent = parent
                del node

                # after every deletion we have to check tree balance
                self.handle_violation(parent)

            else:
                print("Removing the node with two children")

                predecessor = self.get_predecessor(node=node)
                node.data, predecessor.data = predecessor.data, node.data

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node

    def handle_violation(self, node: Node):
        # check the nodes from the node we have inserted up to root node
        while node:
            node.height = max(
                self.calculate_height(node.left_child),
                self.calculate_height(node.right_child)
            ) + 1
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        balance = self.calculate_balance(node)

        # case left heavy, but left-right heavy or left-left heavy
        if balance > 1:
            # left-right heavy situation => left rotation on parent +
            # right rotation on grandparent
            if self.calculate_balance(node.left_child) < 0:
                self.rotate_left(node.left_child)

            # right rotation on grandparent for both: left-right heavy or
            # left-left heavy
            self.rotate_right(node)

        # case right heavy, but right-left heavy or right-right heavy
        if balance < -1:
            # right-left heavy situation => right rotation on parent +
            # left rotation on grandparent
            if self.calculate_balance(node.right_child) > 0:
                self.rotate_right(node.right_child)

            # left rotation on grandparent for both: right-left heavy or
            # right-right heavy
            self.rotate_left(node)

    def calculate_height(self, node: Node) -> int:
        if not node:
            return -1
        return node.height

    def calculate_balance(self, node: Node) -> int:
        if not node:
            return 0

        return self.calculate_height(node.left_child) - self.calculate_height(node.right_child)

    def rotate_left(self, node: Node):
        pass

    def rotate_right(self, node: Node):
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
