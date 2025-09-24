# // n = 10 nodes
# // edges = [[1 2] , [1 3] , [2 4] , [3 5] , [7 8]]
import collections
import math
def dfs(node,visited,graph):
    
    neighbors = graph[node]
    if not neighbors:
        return 0
    res = 1
    visited[node] = True
    for item in neighbors:
        if not visited[item]:
            res += dfs(item,visited,graph)
        
    return res
def cloudFront(n, edges):
    # build graph
    graph = collections.defaultdict(set)
    for each in edges:
        graph[each[0]].add(each[1])
        graph[each[1]].add(each[0])
    visited = [ False for _ in range(n+1)]
    nodes = graph.keys()
    count = 0
    acc = 0
    ret = 0
    for node in nodes:
        if not visited[node]:
            count = dfs(node,visited,graph)
            print(count)
            acc += count 
            ret += math.ceil(math.sqrt(count))
    print(acc,ret,n)
    
    return int(ret + n - acc)
        
    

print(cloudFront(10,[[1, 2] , [1, 3] , [2, 4] , [3, 5] , [7,8]]))

        
        
    
    
