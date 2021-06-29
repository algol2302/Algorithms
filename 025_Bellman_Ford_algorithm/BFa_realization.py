class Edge:

    def __init__(
        self, weight: int, start_vertex, target_vertex
    ) -> None:
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:

    def __init__(self, name: str):
        self.name = name
        self.adjacency_list = []
        self.predecessor = None
        self.min_distance = float('inf')


class BellmanFordAlgorithm:

    def __int__(
        self,
        vertex_list: list[Node],
        edge_list: list[Edge],
        start_vertex: Node
    ) -> None:
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False

    def find_shortest_path(self):
        self.start_vertex.min_distance = 0

        # so we consider V-1 iterations
        # final running time is O(V*N)
        for _ in range(len(self.vertex_list)-1):

            # in every iteration we consider all edges:
            for edge in self.edge_list:
                # we have to calculate whether are there shorter paths:
                u = edge.start_vertex
                v = edge.target_vertex

                dist = u.min_distance + edge.weight

                if dist < v.min_distance:
                    v.predecessor = u
                    v.min_distance = dist

        # after we make V-1 iterations we have to check negative cycles:
        for edge in self.edge_list:
            if self.check_cycle(edge):
                print("Negative cycle detected...")
                return

    def check_cycle(self, edge: Edge):
        # if the total cost (min distance) of the given vertex decreases
        # after V-1 iteration, it means there is a negative cycle graph
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortest_path(self, vertex: Node):

        if not self.has_cycle:
            print(f"Shortest path exists with value: {vertex.min_distance}")
            node = vertex

            while node:
                print(node.name)
                node = node.predecessor
        else:
            print("There is a negative cycle in the G(V, E) graph...")


def main():
    pass


if __name__ == '__main__':
    main()
