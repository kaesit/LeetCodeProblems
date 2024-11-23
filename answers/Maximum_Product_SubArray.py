class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_max = float('-inf')
        current_max,pre,suff = 0, 1, 1
        n = len(nums)
        if n < 2:
            return nums[0]