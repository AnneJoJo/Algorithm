#[[0, 30],[5, 10],[15, 20]]
# how many rooms at least we need?

# 0 5 10 15 20 30
# |_____________|
#    |__| |___|  how many overlap
# 1 1  -1  1  -1 -1 largest subarray sum

class Interval:
    def __init__(self,s,e):
        self.start = s
        self.end = e


def meetingRoom(intervals):
    intervals = sorted(intervals,key=lambda x:x.start)
    for i in range(1,len(intervals)):
        if intervals[i].start < intervals[i-1].end:
            return False

    return True


intervals = [Interval(0,10),Interval(15,20),Interval(30,40)]

print(meetingRoom(intervals))
