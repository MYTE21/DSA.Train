"""
Problem Link: https://leetcode.com/problems/course-schedule/description/
"""
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        visited = set()
        path = set()
        order = []
        for course in range(numCourses):
            if course not in visited:
                visited.add(course)
                if not self.dfs(graph, course, path, order, visited):
                    return False
        return True

    def dfs(self, graph, vertex, path, order, visited):
        path.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor in path:
                return False
            if neighbor not in visited:
                visited.add(neighbor)
                if not self.dfs(graph, neighbor, path, order, visited):
                    return False
        path.remove(vertex)
        order.append(vertex)
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1,0]])) # True
    print(s.canFinish(2, [[1,0],[0,1]])) # False
