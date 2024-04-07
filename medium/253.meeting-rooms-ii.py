#Solution 1
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 04/06/2024
        start = sorted([x[0] for x in intervals ])
        end = sorted([x[1] for x in intervals])

        cur, maxC = 0, 0
        i, j = 0, 0
        while i < len(start):
            if start[i] < end[j]:
                # start happens befor a end, concurrent meeting +1
                cur += 1
                maxC = max(maxC, cur)
                i += 1
            else:
                # start==end, a meeting end a new meeting start, end meeting first
                # start>end, a meeting end
                cur -= 1
                j += 1
        return maxC
# Solution 2
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 04/06/2024
        intervals = sorted(intervals, key=lambda x:x[0])
        heap = []
        for itv in intervals:
            if not heap or itv[0] < heap[0]:
                # need new room
                heapq.heappush(heap, itv[1])
            else:
                heapq.heapreplace(heap, itv[1])
        return len(heap)