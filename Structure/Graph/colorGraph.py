'''
Not a graph. It's a backtracking problem

'''
class Graph():
    def __init__(self, v, matrix):
        self.vertex = v
        self.graph = matrix  ## adjacency matrix


class Solution:
    def color_graph(self, g, m):

        path = [0] * g.vertex  ## initial an array to save the color condition

        return self.backtrack(g.vertex, m, path, 0,g)


    def backtrack(self, v_n, m, path, idx,g):

        if 0 not in path:
            return True
        res = False
        for i in range(1,m+1):

            if self.can_color(i,idx,g,path):
                path[idx] = i
                res = self.backtrack(v_n, m, path, idx + 1,g)
                path[idx] = 0
        if res:
            return True
        else:
            return False


    def can_color(self, i_c, idx_v, graph,path):

        for col in range(len(graph.graph[idx_v])):
            if graph.graph[idx_v][col] == 1 and path[col] == i_c:
                return False
        return True


matrix = [[0,0,0,0,0,0,1,0,0],[0,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0],[0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0]]
g = Graph(9,matrix)
s = Solution()
print(s.color_graph(g,1))


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()

    while True:
         try:
             line = lines.next()
         except StopIteration:
             break

if __name__ == '__main__':
    main()