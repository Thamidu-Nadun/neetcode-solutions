class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            h = heights[i]
            rw = 0
            lw = 0
            
            # right most
            for r in range(i+1, len(heights)):
                if heights[r] < h:
                    break
                rw += 1
                
            # left most
            if i != 0:
                for l in range(i-1, -1, -1):
                    if heights[l] < h:
                        break
                    lw += 1
            area = h * (lw+rw+1)
            areas.append(area)
            
        return max(areas)