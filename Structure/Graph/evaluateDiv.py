import collections
def evaluateDiv(equations,values,query):
    """

    :param equations: list
    :param values: list
    :param query: list
    :return: list
    """

    res = []
    #build graph
    graph = collections.defaultdict(list)
    for idx, each in enumerate(equations):
        graph[each[0]].append([values[idx],each[1]])
        graph[each[1]].append([1/values[idx],each[0]])
    print(graph)
    for q in query:
        print(q[0],q[1],'q')
        res.append(dfs(graph,q[0],q[1],1,set()))

    return  res

def dfs(graph,cur,end,acc,visited):
    if end not in graph.keys():
        return -1.0
    if cur == end :
        return acc
    visited.add(cur)

    if cur in graph.keys():
        neighbors = graph[cur]
        print(cur,'before')
        for n in neighbors:
            if n[1] in visited:
                continue
            print(acc*n[0],visited,end,n[1])
            ret = dfs(graph,n[1],end,acc*n[0],visited)
            if ret != -1.0:
                return ret

    return  -1.0





equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
query = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

print(evaluateDiv(equations,values,query))

