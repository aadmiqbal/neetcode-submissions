class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        brackets = []
        if s == "":
            return True
        for c in s:
            if c in dic:
                brackets.append(c)
            elif c in dic.values():
                if len(brackets) == 0:
                    return False
                if dic[brackets.pop()] != c:
                    return False
            else:
                return False
        if len(brackets) != 0:
            return False
        return True

