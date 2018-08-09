"""Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = nums.sort()
        print(a)
        prev = None
        temp = 0
        for num in nums:
            if prev == num:
                temp = 5
            prev = num
            
        if temp == 5:
            return True
        else:
            return False


#easy solution is:  return len(set(nums)) != len(nums)