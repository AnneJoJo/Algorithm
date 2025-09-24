import heapq
class ScheduleDeliveries(object):
    def solution(self, n, open_times, delivery_time_cost):
        hq =[]
        for t in open_times:
            heapq.heappush(hq,t) 
        delivery_time_cost.sort(reverse = True) 
        res = 0
        m = len(delivery_time_cost)
        for i in range(0,m,4):
            t = heapq.heappop(hq)
            t += delivery_time_cost[i]
            res = max(t, res) 
            heapq.heappush(hq,t)
        return res
s = ScheduleDeliveries()    
print(s.solution(2,[7,9], [7,6,3,4,1,1,2,0]))

