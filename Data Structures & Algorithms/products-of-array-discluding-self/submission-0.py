"""
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            out.append(prod)
        
        return out
