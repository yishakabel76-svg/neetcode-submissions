class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        res_max = 0
        window = []
        for right in range(len(nums)):
            window.append(nums[right])
            if right - left + 1 == k:
                res.append(max(window))
                window.remove(nums[left])
                left += 1
        return res