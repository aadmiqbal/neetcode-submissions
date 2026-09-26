class Solution:
    def isValid(self, s: str) -> bool:
        pairs= {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        s_list = list(s)
        new_s = []
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        try:
            for b in s:
                if b in pairs:
                    new_s.append(b)
                elif b in pairs.values():
                    if b != pairs[new_s.pop()]:
                        return False
        except Exception as e:
            return False
        if len(new_s) > 0:
            return False
        return True
                    
