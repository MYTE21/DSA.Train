def topological_sort(graph):
    in_degree = {u: 0 for u in graph}

    for key, value in graph.items():
        for item in value:
            in_degree[item] += 1

    # BFS
    queue = [u for u in graph if in_degree[u] == 0]
    top_order = []

    while queue:
        u = queue.pop(0)
        top_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(top_order) != len(graph):
        raise ValueError("The graph has a cycle..!")

    return top_order


if __name__ == "__main__":
    dict_graph = {
        "Breakfast": ["Office"],
        "Dress up": ["Office"],
        "Office": ["Dinner", "Sports", "Email"],
        "Dinner": ["Sports"],
        "Email": ["Dinner", "Sports"],
        "Sports": []
    }

    top_sort = topological_sort(dict_graph)
    print(top_sort)
