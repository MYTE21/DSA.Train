def depth_first_search(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            depth_first_search(graph, neighbour, visited)


if __name__ == "__main__":
    source_graph = {
        "5": ["3", "7"],
        "3": ["2", "4"],
        "7": ["8"],
        "2": [],
        "4": ["8"],
        "8": []
    }
    source_node = "5"
    visited_node = set()

    print("Depth First Search: ")
    depth_first_search(source_graph, source_node, visited_node)