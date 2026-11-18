class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # i = 0
        # n = len(intervals)
        # while i+1 < n and (intervals[i+1][0] <= intervals[i][1] or intervals[i+1][1] <=  intervals[i][1]):
        #     intervals[i][0] = min(intervals[i+1][0], intervals[i][0])
        #     intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
        #     intervals.pop(i+1)
        #     i += 1
        # return intervals
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastend = output[-1][1]

            if start <= lastend:
                output[-1][1] = max(lastend,end)
            else:
                output.append([start,end])
        return output


