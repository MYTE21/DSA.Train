def breath_first_search(graph, node):
    queue = []
    visited = []

    queue.append(node)
    visited.append(node)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


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

    breath_first_search(source_graph, source_node)