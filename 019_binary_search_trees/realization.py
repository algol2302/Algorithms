from numbers import Number
from typing import Any


class Node:

    def __init__(self, data: Number, parent: Any):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent

    def __repr__(self):
        return f"Node with data: {self.data!r}"


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data: Number) -> None:
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data: Number, node: Node) -> None:
        # we have to go to left subtree
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        # we have to go to right subtree
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)

    def traverse(self) -> None:
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node: Node) -> None:

        # first left child
        if node.left_child:
            self.traverse_in_order(node.left_child)

        # second parent node
        print(node.data)

        # third right child
        if node.right_child:
            self.traverse_in_order(node.right_child)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node: Node) -> Number:
        # recursion solution:
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data

        # loop solution
        # actual = node
        #
        # while actual.right_child is not None:
        #     actual = actual.right_child
        #
        # return actual.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node: Node) -> Number:
        # recurse solution:
        # if node.left_child:
        #     return self.get_min(node.left_child)
        # return node.data

        # loop solution:
        actual = node

        while actual.left_child is not None:
            actual = actual.left_child

        return actual.data

    def remove(self, data: Number):
        if self.root:
            self.remove_node(data=data, node=self.root)

    def remove_node(self, data: Number, node: Node):
        if not node:
            return

        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:

            if not node.left_child and not node.right_child:
                print(f"Removing leaf {node}")

                parent = node.parent

                if parent and parent.left_child == node:
                    parent.left_child = None

                if parent and parent.right_child == node:
                    parent.right_child = None

                if not parent:
                    self.root = None

                del node

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

            else:
                print("Removing the node with two children")

                predecessor = self.get_predecessor(node=node)
                node.data, predecessor.data = predecessor.data, node.data

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node


def main():
    bst = BinarySearchTree()
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
