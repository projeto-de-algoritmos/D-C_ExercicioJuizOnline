class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2

        max_left_sum = self.maxSubArray(nums[:mid])
        max_right_sum = self.maxSubArray(nums[mid:])

        max_cross_sum = self.maxCrossingSum(nums, mid)

        return max(max_left_sum, max_right_sum, max_cross_sum)

    def maxCrossingSum(self, nums, mid):
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid - 1, -1, -1):
            current_sum += nums[i]
            left_sum = max(left_sum, current_sum)

        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid, len(nums)):
            current_sum += nums[i]
            right_sum = max(right_sum, current_sum)

        return left_sum + right_sum