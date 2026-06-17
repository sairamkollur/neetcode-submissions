class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for character in s:
            # If current character is a closing bracket
            if character in closeToOpen:

                # Check stack is not empty
                # and top of stack matches opening bracket
                if stack and stack[-1] == closeToOpen[character]:
                    stack.pop()
                else:
                    return False

            # Opening bracket
            else:
                stack.append(character)

        return True if not stack else False