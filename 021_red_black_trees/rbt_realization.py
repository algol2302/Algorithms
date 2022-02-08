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
            self.settle_violation(self.root)
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

    def traverse(self):
        if self.root:
            self.in_order_traversal(self.root)

    def in_order_traversal(self, node: Node):

        if node.left_node:
            self.in_order_traversal(node.left_node)

        print(node)

        if node.right_node:
            self.in_order_traversal(node.right_node)

    def rotate_right(self, node: Node):
        print(f"Rotating to the right on {node}")

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        # update parents
        if t:
            t.parent = node

        node.parent, temp_left_node.parent = temp_left_node, node.parent

        # update childs for ex parent of the node
        if temp_left_node.parent and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        # update root
        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self, node: Node):
        print(f"Rotating to the left on {node}")

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        # update parents
        if t:
            t.parent = node

        node.parent, temp_right_node.parent = temp_right_node, node.parent

        # update childs for ex parent of the node
        if temp_right_node.parent and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if (
            temp_right_node.parent
            and temp_right_node.parent.right_node == node
        ):
            temp_right_node.parent.right_node = temp_right_node

        # update root
        if node == self.root:
            self.root = temp_right_node

    def settle_violation(self, node: Node):

        while (
            node != self.root
            and self.is_red(node)
            and self.is_red(node.parent)
        ):
            parent_node = node.parent
            grand_parent_node = parent_node.parent

            # parent is a left child of it's parent (so the grandparent)
            if parent_node == grand_parent_node.left_node:
                uncle = grand_parent_node.right_node

                if uncle and self.is_red(uncle):
                    # case 1.) and case 4.) RECOLORING
                    print(f"Re-coloring node {grand_parent_node.data} to Red")
                    grand_parent_node.color = Color.RED
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                else:
                    # case 2. uncle node is black and node is a right child
                    if node == parent_node.right_node:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # case 3. rotation on the grandparent + parent and
                    # grandparent switch color
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print(f"Re-coloring node {parent_node.data} to Black")
                    print(f"Re-coloring node {grand_parent_node.data} to Red")
                    self.rotate_right(grand_parent_node)

            else:
                uncle = grand_parent_node.left_node

                if uncle and self.is_red(uncle):
                    # case 1.) and case 4.) RECOLORING
                    print(f"Re-coloring node {grand_parent_node.data} to Red")
                    grand_parent_node.color = Color.RED
                    print(f"Re-coloring node {parent_node.data} to Black")
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                else:
                    # case 2. uncle node is black and node is a right child
                    if node == parent_node.left_node:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # case 3. rotation on the grandparent + parent and
                    # grandparent switch color
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print(f"Re-coloring node {parent_node.data} to Black")
                    print(f"Re-coloring node {grand_parent_node.data} to Red")
                    self.rotate_left(grand_parent_node)

        if self.is_red(self.root):
            print(f"Re-coloring the root {self.root.data} to Black")
            self.root.color = Color.BLACK

    def is_red(self, node: Node):
        if not node:
            return False
        return node.color == Color.RED


def main():
    tree = RedBlackTree()
    tree.insert(32)
    tree.insert(10)
    tree.insert(55)
    tree.insert(1)
    tree.insert(19)
    tree.insert(79)
    tree.insert(16)
    tree.insert(23)
    tree.insert(12)


if __name__ == "__main__":
    main()
