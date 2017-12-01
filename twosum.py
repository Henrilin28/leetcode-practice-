class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return false
        else:
            dic = {}
            for i, num in enumerate(nums):
                if num in dic:
                    return [dic[num], i]
                else:
                    dic[target - num] = i
