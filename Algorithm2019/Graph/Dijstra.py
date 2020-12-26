import heapq
def dijs(graph,n):
    visited = [0]*n
    dist = [float('inf')] * n
    heap = [[0,0]]
    heapq.heapify(heap)
    print(graph)
    while heap:
        cur_node, cur_dist = heapq.heappop(heap)
        print(heap)
        visited[cur_node] = 1
        if cur_node not in graph.keys():continue
        for neighbor in graph[cur_node]:
            next_node,next_dist = neighbor[0],neighbor[1]
            if visited[next_node]: continue
            if next_dist + cur_dist < dist[next_node]:
                dist[next_node] = next_dist + cur_dist
                heap.append([next_node,next_dist + cur_dist])

        heapq.heapify(heap)


    return dist



print(dijs({0:[[1,1]],1:[[3,2],[2,4]],2:[[4,4]],3:[[2,8]]},5))
print(dijs({0:[[1,100],[2,500]],1:[[2,100]]},3))

#787. Cheapest Flights Within K Stops
# There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#   0
# /  \
# 1 --2
