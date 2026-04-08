class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif stack:
                if i == '}' and stack[-1] != '{':
                    return False
                elif i == ']' and stack[-1] != '[':
                    return False
                elif i == ')' and stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            else:
                return False
        print(stack)
        return True if stack == [] else False