class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

def merge_intervals(Intervals):
    """
    
    :param Intervals: list contains interval class
    :return: list (res)
    [[1,3],[5,8],[4,10],[20,25]]
    """
    if Intervals == [] or len(Intervals) == 0:
        return []

    res = []
    start = Intervals[0].start
    end = Intervals[0].end

    for each in Intervals[1::]:

        if each.start <= end:
            tmp_st = min(start,each.start)
            tmp_ed = max(end,each.end)

            start = tmp_st
            end = tmp_ed

            continue
        else:
            res.append([start,end])
            start = each.start
            end = each.end
    res.append([start,end])

    return  res

a = [Interval(1,3),Interval(3,8),Interval(4,10),Interval(7,25)]

print(merge_intervals(a))