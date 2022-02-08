class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

    def __repr__(self):
        return f"Node: {self.name!r}"


def breadth_first_search(start_node: Node):

    # FIFO
    queue = [start_node]

    # we keep iterating (considering the neighbours) until the queue
    # becomes empty
    while queue:
        actual_node = queue.pop(0)
        print(actual_node)

        # let's consider the neighbours of the actual node one by one:
        for node in actual_node.adjacency_list:
            if not node.visited:
                queue.append(node)


if __name__ == "__main__":

    # we can create the node or vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # we have to handle the neighbours:
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    # run BFS algorithm:
    breadth_first_search(node1)
