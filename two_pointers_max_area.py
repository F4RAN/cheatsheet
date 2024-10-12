"""
Explanation
Since the area is limited by the shorter of the two lines, moving the pointer pointing to the longer line inward won't help in finding a potentially larger area because the height is still constrained by the shorter line. 
Instead, by moving the pointer pointing to the shorter line, there's a chance to find a taller line that could increase the area, even if the width decreases.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointers
        p1 = 0
        p2 = len(height) - 1
        areas = []
        while p1 < p2:
            y1 = height[p1]
            y2 = height[p2]
            areas.append((p2 - p1) * min(y1,y2))
            if y1 > y2:
                p2 -= 1
            else:
                p1 += 1
        return max(areas)


                


