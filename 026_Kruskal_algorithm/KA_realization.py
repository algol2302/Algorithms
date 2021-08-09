from typing import TypeVar

E = TypeVar("E", bound="Edge")
N = TypeVar("N", bound="Node")


class Vertex:

    # this is the node or the vertex in the G(V, E)
    def __init__(self, name: str):
        self.name = name
        # it's the node representation (disjoint sets)
        self.node = None


class Edge:

    def __init__(
            self,
            weight: int,
            start_vertex: Vertex,
            target_vertex: Vertex):

        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    # Kruskal's algorithm sorts the edges by the weights
    # python must know how to compare edges
    def __lt__(self, other_edge: E):
        return self.weight < other_edge.weight


class Node:

    # node in the tree representation of the disjoint sets
    def __init__(self, rank: int, node_id, parent: N):
        self.rank = rank
        self.node_id = node_id
        self.parent = parent


def main():
    pass


if __name__ == '__main__':
    main()
