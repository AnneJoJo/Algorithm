class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        
        """
        import  collections

        def dfs(res, graph, lowestRank, visited, currentRank, pre, cur):
            visited[cur] = 1
            lowestRank[cur] = currentRank
            for nextVertx in graph[cur]:
                if nextVertx == pre:
                    continue
                if visited[nextVertx] == 0:
                    dfs(res, graph, lowestRank, visited, currentRank + 1, cur, nextVertx)

                lowestRank[cur] = min(lowestRank[cur], lowestRank[nextVertx])

                if lowestRank[nextVertx] >= currentRank + 1:  # ****
                    res.append([cur, nextVertx])

        res = []
        lowestRank = [i for i in range(n)]
        graph = collections.defaultdict(list)
        visited = [0] * n
        currentRank = 0
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        pre = -1
        dfs(res, graph, lowestRank, visited, currentRank, pre, 0)
        return res



