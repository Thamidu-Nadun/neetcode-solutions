class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums_set = set(nums)
        max_len = 0
        
        for i in nums_set:
            if i - 1 not in nums_set:
                curr = i
                curr_len = 1
                while curr + 1 in nums_set:
                    curr += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        
        return max_len