INF = float("inf")

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = INF
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def main():
    # initial graph, costs, parents:
    # graph = {
    #     "start": {"a": 6, "b": 2},
    #     "a": {"fin": 1},
    #     "b": {"a": 3, "fin": 5},
    #     "fin": {}
    # }
    #
    # costs = {
    #     "a": 6,
    #     "b": 2,
    #     "fin": INF
    # }
    #
    # parents = {
    #     "a": "start",
    #     "b": "start",
    #     "fin": None
    # }

    graph = {
        "start": {"a": 5, "b": 2},
        "a": {"c": 4, "d": 2},
        "b": {"a": 8, "d": 7},
        "c": {"d": 6, "fin": 3},
        "d": {"fin": 1},
        "fin": {}
    }

    costs = {
        "a": 6,
        "b": 2,
        "c": INF,
        "d": INF,
        "fin": INF
    }

    parents = {
        "a": "start",
        "b": "start",
        "c": None,
        "d": None,
        "fin": None
    }

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost_node(costs)

    print(f"Shortest way: {processed}, cost: {costs['fin']}")


if __name__ == '__main__':
    main()
