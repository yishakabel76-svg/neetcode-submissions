class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         set_num = set(nums)
         max_len = 0
         for x in set_num:
            if x-1 not in set_num:
                current = x
                length=1
                while current + 1 in set_num:
                    current+=1
                    length+=1
                max_len = max(max_len , length)
         return max_len