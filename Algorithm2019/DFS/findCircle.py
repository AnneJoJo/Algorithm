import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dep = collections.defaultdict(list)
        for course, pre in prerequisites:
            dep[pre].append(course)

        visit = set()
        fully_processed = set()  # To avoid reprocessing nodes

        def findCircle(cur, graph):
            if cur in visit:
                return True
            if cur in fully_processed:
                return False

            visit.add(cur)
            if cur in graph:
                for each in graph[cur]:
                    if findCircle(each, graph):
                        return True
            visit.remove(cur)
            fully_processed.add(cur)
            return False

        for i in range(numCourses):
            if findCircle(i, dep):
                return False

        return True
#topological:
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 1 or len(prerequisites) == 0: return True

        # generate graph
        graph = collections.defaultdict(lambda: [], {})
        for c, p in prerequisites:
            graph[c].append(p)

        # initialize indgree of each node
        indgree = [0 for node in range(numCourses)]

        for node in graph:
            indgree[node] = len(graph[node])
        queue = [node for node in range(numCourses) if indgree[node] == 0]
        top_sorted = []
        while queue:
            node_s = queue.pop(0)
            top_sorted.append(node_s)
            # interactive whole graph
            for node, neighbors in graph.items():
                if node_s in neighbors:
                    indgree[node] -= 1
                    if indgree[node] == 0:
                        queue.append(node)
        return len(top_sorted) == numCourses

