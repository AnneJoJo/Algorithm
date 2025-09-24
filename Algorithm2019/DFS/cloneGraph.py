"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        clone = {}
        def cloneNew(node):
            if node in clone:
                return clone[node]

            deepCopy = Node(node.val,[])
            clone[node] = deepCopy
            for each in node.neighbors:
                deepCopy.neighbors.append(cloneNew(each))

            return deepCopy

        return cloneNew(node) if node else None









