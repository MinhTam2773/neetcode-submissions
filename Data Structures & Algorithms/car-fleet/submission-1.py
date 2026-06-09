class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        for p, s in reversed(sorted(list(zip(position,speed)))):
            t = (target - p) / s
            
            if not stack or stack[-1] < t:
                stack.append(t)
    
        for item in stack:
            print(item)
        return len(stack)