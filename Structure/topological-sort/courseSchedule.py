import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Correctly build the graph: course -> list of prerequisites (integers)
        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)  #Append the prerequisite integer

        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def has_cycle(node):
            if visited[node] == 1:
                return True  # Cycle detected
            if visited[node] == 2:
                return False  # Already processed
            
            visited[node] = 1  # Mark as being visited
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            visited[node] = 2  # Mark as fully processed
            return False

        for course in range(numCourses):
            if visited[course] == 0 and has_cycle(course):
                return False
        return True