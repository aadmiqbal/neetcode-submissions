class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        stack = []

        for i in range(len(s)):
            if s[i] in dic:
                stack.append(s[i])
            elif s[i] in dic.values():
                match s[i]:
                    case "}":
                        if len(stack) < 1 or stack.pop() != "{":
                            return False
                    case ")":
                        if len(stack) < 1 or stack.pop() != "(":
                            return False
                    case "]":
                        if len(stack) < 1 or stack.pop() != "[":
                            return False
            else:
                return False

        if len(stack) > 0:
            return False

        return True


