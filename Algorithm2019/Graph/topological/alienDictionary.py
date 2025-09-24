import collections
def alienDictionary(arr):
    if len(arr) == 0:return ''
    # build a graph
    graph = collections.defaultdict(list)
    indgree = collections.defaultdict(int)
    for word in arr:
            for w in word:
                indgree[w] = 0
    for i in range(len(arr)-1):
        first, sed = arr[i], arr[i+1]
        tmpLen = min(len(first),len(sed))
        j = 0
        while j < tmpLen:
            if first[j] != sed[j]:
                graph[first[j]].append(sed[j])
                indgree[first[j]] += 1
            j += 1
    queue = [ k for k, v in indgree.items() if v == 0 ]
    ret = []
    while queue:
        curNode = queue.pop()
        neighbor = graph[curNode]
        for n in neighbor:
            indgree[n] -= 1
            if indgree[n] == 0:
                queue.append(n)
        del graph[curNode]
    if len(graph) > 0:
        return ""
    return ''.join(str(i) for i in ret)
        
        
        
            
        