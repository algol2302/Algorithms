from realization import BinarySearchTree, Node


def compare_trees(node_1: Node, node_2: Node) -> bool:
    if not node_1 or not node_2:
        return node_1 == node_2

    if node_1.data != node_2.data:
        return False

    return compare_trees(
        node_1.left_child, node_2.left_child
    ) and compare_trees(node_1.right_child, node_2.right_child)


def main():
    bst_1 = BinarySearchTree()
    bst_1.insert(10)
    bst_1.insert(5)
    bst_1.insert(-5)
    bst_1.insert(1)
    bst_1.insert(99)
    bst_1.insert(34)
    bst_1.insert(1000)

    bst_2 = BinarySearchTree()
    bst_2.insert(10)
    bst_2.insert(5)
    bst_2.insert(-4)
    bst_2.insert(1)
    bst_2.insert(99)
    bst_2.insert(34)
    bst_2.insert(1000)

    relation = (
        "is the same as"
        if compare_trees(bst_1.root, bst_2.root)
        else "isn't the same as"
    )
    print(f"Comparison: bst_1 {relation} bst2")


if __name__ == "__main__":
    main()
