
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res  = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[str(count)].append(s)
        
        newlist = []
        for x in res.values():
            newlist.append(x)
        return newlist
