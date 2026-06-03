class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for l in range(n-1):
            for r in range(n-1, l, -1):
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
        return []