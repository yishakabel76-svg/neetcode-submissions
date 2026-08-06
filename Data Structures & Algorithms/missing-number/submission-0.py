class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        for n in nums:
            summ +=n
        amount = len(nums)
        cur_sum = amount*(amount+1)/2
        return int(cur_sum - summ) 

