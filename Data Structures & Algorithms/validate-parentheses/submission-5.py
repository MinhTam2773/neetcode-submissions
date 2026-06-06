class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]":"[", "}" : "{"}
        for braket in s:
            if braket in close_to_open:
                if stack and stack[-1] == close_to_open[braket]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(braket)
        if stack:
            return False
        return True