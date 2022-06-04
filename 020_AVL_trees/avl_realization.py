from typing import Any
from numbers import Number


class Node:
    def __init__(self, data: Number, parent: Any):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.height = 0

    def __repr__(self):
        return f"node with data: {self.data!r}"

    def all_data(self):
        return (
            f"Node with data: {self.data}, "
            f"Left {self.left_child}, "
            f"Parent {self.parent}, "
            f"Right {self.right_child}, "
            f"Height: {self.height}"
        )


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
                node.height = (
                    max(
                        self.calculate_height(node.left_child),
                        self.calculate_height(node.right_child),
                    )
                    + 1
                )
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)
                node.height = (
                    max(
                        self.calculate_height(node.left_child),
                        self.calculate_height(node.right_child),
                    )
                    + 1
                )

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
            node.height = (
                max(
                    self.calculate_height(node.left_child),
                    self.calculate_height(node.right_child),
                )
                + 1
            )
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

        return self.calculate_height(node.left_child) - self.calculate_height(
            node.right_child
        )

    def rotate_left(self, node: Node):
        print(f"Rotating to the left on {node}")

        temp_right_child = node.right_child
        t = temp_right_child.left_child

        temp_right_child.left_child = node
        node.right_child = t

        # update parents
        if t:
            t.parent = node

        node.parent, temp_right_child.parent = temp_right_child, node.parent

        # update childs for ex parent of the node
        if (
            temp_right_child.parent
            and temp_right_child.parent.left_child == node
        ):
            temp_right_child.parent.left_child = temp_right_child

        if (
            temp_right_child.parent
            and temp_right_child.parent.right_child == node
        ):
            temp_right_child.parent.right_child = temp_right_child

        # case node is root
        if node == self.root:
            self.root = temp_right_child

        # recalculate heights
        node.height = (
            max(
                self.calculate_height(node.left_child),
                self.calculate_height(node.right_child),
            )
            + 1
        )
        temp_right_child.height = (
            max(
                self.calculate_height(temp_right_child.left_child),
                self.calculate_height(temp_right_child.right_child),
            )
            + 1
        )

    def rotate_right(self, node: Node):
        print(f"Rotating to the right on {node}")

        temp_left_child = node.left_child
        t = temp_left_child.right_child

        temp_left_child.right_child = node
        node.left_child = t

        # update parents
        if t:
            t.parent = node

        node.parent, temp_left_child.parent = temp_left_child, node.parent

        # update childs for ex parent of the node
        if (
            temp_left_child.parent
            and temp_left_child.parent.left_child == node
        ):
            temp_left_child.parent.left_child = temp_left_child

        if (
            temp_left_child.parent
            and temp_left_child.parent.right_child == node
        ):
            temp_left_child.parent.right_child = temp_left_child

        # update root
        if node == self.root:
            self.root = temp_left_child

        # recalculate heights
        node.height = (
            max(
                self.calculate_height(node.left_child),
                self.calculate_height(node.right_child),
            )
            + 1
        )
        temp_left_child.height = (
            max(
                self.calculate_height(temp_left_child.left_child),
                self.calculate_height(temp_left_child.right_child),
            )
            + 1
        )

    def traverse(self) -> None:
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node: Node) -> None:

        # first left child
        if node.left_child:
            self.traverse_in_order(node.left_child)

        # second parent node
        print(node.all_data())

        # third right child
        if node.right_child:
            self.traverse_in_order(node.right_child)


def main():
    avl = AVLTree()
    avl.insert(5)
    # 1. left-right unbalanced tree:
    # avl.insert(3)
    # avl.insert(4)
    # 2. right-left unbalanced tree:
    # avl.insert(8)
    # avl.insert(6)
    # 3. balanced tree
    avl.insert(3)
    avl.insert(10)
    avl.insert(2)
    avl.insert(4)
    avl.insert(15)
    # 4. removing
    avl.remove(15)
    avl.remove(10)
    # show
    avl.traverse()


if __name__ == "__main__":
    main()
