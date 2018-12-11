"""Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59."""

 def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints = map(lambda x: int(x.split(":")[0])*60 + int(x.split(":")[1]), timePoints)
        timePoints = sorted(timePoints)
        
        timePoints.append(timePoints[0]+24*60)
    
        res  = float('inf')
        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i]-timePoints[i-1])
        return res