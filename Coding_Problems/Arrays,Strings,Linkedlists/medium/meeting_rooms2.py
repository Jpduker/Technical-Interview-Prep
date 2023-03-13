from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        #count of ongoing meetings and max will be stored in res
        res,ongoing =0,0
        
        #two pointers which points to start of both start and end lists 
        s,e =0,0

        while s<len(intervals):
            if start[s] < end[e]:
                ongoing+=1
                s+=1
            else:
                ongoing -=1
                e+=1
            res = max(res,ongoing)
        return res
        
