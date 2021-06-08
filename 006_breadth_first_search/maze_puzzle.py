"""Using BFS to find way out of maze"""


class Node:

    def __init__(self, index_x, index_y):
        self.index_x = index_x
        self.index_y = index_y
        self.adjacency_list = []
        self.visited = False

    def __repr__(self):
        return f"({self.index_x!r}, {self.index_y!r})"


def breadth_first_search(start_node):
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


def main():
    # start and destination points:
    start = (0, 0)
    destination = (4, 4)

    # maze:
    maze = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    # TODO finish it


if __name__ == '__main__':
    main()
