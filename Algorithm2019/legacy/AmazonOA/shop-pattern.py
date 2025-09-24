from collections import defaultdict 
def shopPattern(product_nodes,edges):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    d = {n:len(graph[n]) for n in graph} # save the count of node
    print(d)
    res = float('inf')
    for a in graph.keys():
        for b in graph[a]:
            for c in graph[a] & graph[b]: # if c found in both a:() and b() which means they are trios
                res = min(res, d[a]+d[b]+d[c]-6) #add them all 3 nodes are themself, but it's undirected, so double 3nodes
                graph[c].discard(a) # delete the related nodes once you chekced it
                graph[b].discard(b)
        if res == float('inf'):
            return -1
   # print(res)
    return res
        
shopPattern(3,[[1,2],[2,3],[1,3]])
    # 1 : 2, 3
    # 2:  1, 3
    # 3: 1, 2