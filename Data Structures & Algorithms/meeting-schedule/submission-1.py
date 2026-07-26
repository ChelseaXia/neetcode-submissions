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
        # [a, b], [c, d]
        # 只可能相邻的两个会议发生冲突
        for i in range(1, len(intervals)):
            prev_end, cur_start = intervals[i-1].end, intervals[i].start
            if prev_end > cur_start:
                return False
        return True

            