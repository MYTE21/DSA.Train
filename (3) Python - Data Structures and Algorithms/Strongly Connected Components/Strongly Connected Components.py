"""
Kosaraju's algorithm to find strongly connected components in Python
Link: https://www.programiz.com/dsa/strongly-connected-components
Extra Link: https://www.geeksforgeeks.org/strongly-connected-components/
"""
from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertex_no):
        self.vertex = vertex_no    # No. of vertices
        self.graph = defaultdict(list)    # default dictionary to store graph

    # Add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # DFS
    def dfs(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v, end=" ")

        # Recursion for all the vertices adjacent to this node
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def fill_order(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True

        # Recursion for all the vertices adjacent to this node
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)

        stack = stack.append(v)

    # Reverse (transpose) of this graph
    def transpose(self):
        g = Graph(self.vertex)

        # Recursion for all the vertices adjacent to this node
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # The main function that finds and prints all strongly connected components
    def print_scc(self):
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * self.vertex

        # Fill vertices in stack according to their finishing times
        for i in range(self.vertex):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        # Create a reversed graph
        gr = self.transpose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * self.vertex

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.dfs(i, visited)
                print("")


if __name__ == "__main__":
    graph = Graph(8)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 0)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)
    graph.add_edge(6, 7)

    print("Strongly Connected Components:")
    graph.print_scc()
