class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = set()
        n = len(heights)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                width = abs(j - i)
                height = min(heights[i], heights[j])
                areas.add(width * height)
        return max(areas)