"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)
        a, b = intervals[0].start, intervals[0].end
        # [a, b], [c, d]
        # 只可能相邻的两个会议发生冲突
        for i in range(1, n):
            c, d = intervals[i].start, intervals[i].end
            if b>c: return False
            a, b = c, d
        return True

            