class Node:

    def __init__(self, name: str) -> None:
        self.name = name
        self.adjacency_list = []
        self.visited = False

    def __repr__(self):
        return f"Node with the name: {self.name!r}"


def depth_first_search(start_node: Node) -> None:

    # that we need a LIFO: last item we insert is the first one
    # we take out
    stack = [start_node]

    # let's iterate until the stack becomes empty
    while stack:
        actual_node = stack.pop()  # O(1)
        actual_node.visited = True
        print(actual_node)

        for node in actual_node.adjacency_list:
            if not node.visited:
                node.visited = True
                # insert the item into the stack
                stack.append(node)


def main():

    # first we have to create the node or vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # handle and set the neighbours accordingly
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    # run DFS
    depth_first_search(node1)


if __name__ == '__main__':
    main()
