# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
        # [[1,3],[2,6],[8,10],[15,18]]
        # [[1,4],[4,5]]
        #[[1,4],[0,4]]
        #[[1,4],[2,3]]
        #[[1,4],[5,6]]  -> NON-LAPPING ARRAY
        # [[1,4],[0,2],[3,5]]
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals)
        # [[0,2],[1,4],[3,5]]
        res = [] # [[0,4],
        for i in range(1,len(intervals)):##############
     #                          3                 4
            if res and intervals[i][0] <= res[-1][1]:
                if res[-1][1] >= intervals[i][1]:
                    continue
                else:
                    res.append([res.pop()[0],intervals[i][1]]) #########
            
            elif intervals[i-1][1] >= intervals[i][0]:
                res.append([intervals[i-1][0],max(intervals[i][1],intervals[i-1][1])]) # [[0,4],
                
            else:
                res.append(intervals[i])  
                
        if intervals[0][1] < intervals[1][0]: # if first to intervals never overlapped
            res = [intervals[0]]+res[:]
                
        return res
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         for i in range(len(intervals)-1):
#             if intervals[i][-1]>=intervals[i+1][0]:
#                 intervals[i]=[intervals[i][0],intervals[i+1][-1]]
#         # intervals.pop(1)
#         return intervals

if __name__=="__main__":
     intervals=[[1,4],[0,2],[3,5]]
     print(merge(intervals))

# intervals=[[1,4],[0,4]]
# if sum(intervals[0])>sum(intervals[1]):
#     print(intervals[1])

# res=[[3,2],[0,4],[1,2]]
# # intervals=[[0,2],[1,4],[3,5]]
# #   4          3                  4
# # if -300000034784738 and 3 <= 4:
# #      print("jjj")
# # res.pop()[0]
# print(res.pop()[:])